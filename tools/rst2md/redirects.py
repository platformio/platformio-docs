# Copyright (c) 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Writes redirects.json: legacy Sphinx URLs -> new Docusaurus pages.

Run after convert.py and scripts/docspregen.py, so every target can be
checked against the pages that exist. Fails if a target is missing.

    python tools/rst2md/redirects.py
"""

import json
import os
import sys

import mapping

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(ROOT, "docs")
REPORT = os.path.join(HERE, "out", "report.json")
OUTPUT = os.path.join(ROOT, "redirects.json")

# Version paths of the legacy Read the Docs site, plus its "/page/" short links
LEGACY_PREFIXES = ("", "/en/latest", "/en/stable", "/page")

# Section page for a legacy redirect whose target was removed earlier
LEGACY_FALLBACKS = (
    ("core/userguide/", "core/userguide/index"),
    ("userguide/", "core/userguide/index"),
    ("integration/ci/", "integration/ci/index"),
    ("ci/", "integration/ci/index"),
)

# Parent page for a generated page that no longer exists
FALLBACKS = (
    ("hardware/boards/", "hardware/boards/index"),
    ("hardware/platforms/", "hardware/platforms/index"),
    ("hardware/frameworks/", "hardware/frameworks/index"),
)


def page_exists(path):
    base = os.path.join(DOCS, path)
    return os.path.isfile(base + ".md") or os.path.isfile(base + ".mdx")


def resolve_target(path):
    if page_exists(path):
        return path
    for prefix, fallback in FALLBACKS:
        if path.startswith(prefix):
            return fallback
    return None


def legacy_froms(docname):
    """Legacy URL paths of a page. The redirects plugin writes "/x" as
    "x/index.html" and "/x.html" as "x.html.html"; with the usual Docusaurus
    server rule "try_files $uri $uri.html $uri/" both spellings resolve."""
    paths = ["/" + docname, "/%s.html" % docname]
    if docname.endswith("/index"):
        paths.append("/" + docname[: -len("/index")])
    result = []
    for prefix in LEGACY_PREFIXES:
        for path in paths:
            if prefix == "" and path in ("/index", "/index.html"):
                continue
            result.append(prefix + path)
    return result


def load_legacy_redirects():
    """Old Sphinx redirects.txt: "/old.html -> /new.html" per line."""
    result = {}
    path = os.path.join(ROOT, "redirects.txt")
    if not os.path.isfile(path):
        return result
    with open(path) as fp:
        for line in fp:
            if "->" not in line or not line.strip().startswith("/"):
                continue
            old, new = (p.strip() for p in line.split("->"))
            result[old[1:].removesuffix(".html")] = new[1:].split("#")[0].removesuffix(".html")
    return result


def resolve_legacy(old, legacy, docs):
    """Follows redirects.txt chains to a legacy docname that still exists."""
    seen = set()
    name = old
    while name in legacy and name not in seen:
        seen.add(name)
        name = legacy[name]
        for candidate in (name, name + "/index"):
            if candidate in docs:
                return candidate
    for prefix, fallback in LEGACY_FALLBACKS:
        if old.startswith(prefix) or name.startswith(prefix):
            return fallback
    return None


def main():
    with open(REPORT) as fp:
        docs = json.load(fp)["docs"]

    targets = {}  # new url -> set of legacy paths
    missing = []
    sources = {d: p for d, p in docs.items() if not mapping.is_partial(d)}
    legacy = load_legacy_redirects()
    for old in legacy:
        new_docname = resolve_legacy(old, legacy, docs)
        if new_docname:
            sources[old] = docs[new_docname]
        else:
            missing.append("redirects.txt: %s -> %s" % (old, legacy[old]))

    for docname, path in sorted(sources.items()):
        if docname == "index":
            continue
        target = resolve_target(path)
        if target is None:
            missing.append("%s -> %s" % (docname, path))
            continue
        url = mapping.doc_url(target)
        targets.setdefault(url, set()).update(
            p for p in legacy_froms(docname) if p != url
        )

    if missing:
        print("Redirect targets that do not exist:", file=sys.stderr)
        for item in missing:
            print("  " + item, file=sys.stderr)
        return 1

    redirects = [
        {"to": url, "from": sorted(froms)}
        for url, froms in sorted(targets.items())
        if froms
    ]
    with open(OUTPUT, "w") as fp:
        json.dump(redirects, fp, indent=1)
        fp.write("\n")
    print(
        "Wrote %d redirects to %d pages: %s"
        % (sum(len(r["from"]) for r in redirects), len(redirects), OUTPUT)
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

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

"""Verifies the conversion against the legacy sources (Phase 1 checks).

1. Every legacy page has a Markdown page (or a generated one).
2. Every code block of a legacy page appears byte-identical in its page.

    python tools/rst2md/check.py
"""

import collections
import json
import os
import re
import sys

import mapping

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(ROOT, "docs")
REPORT = os.path.join(HERE, "out", "report.json")

FENCE_RE = re.compile(r"^(?P<indent> *)(?P<fence>`{3,})[^\n]*\n(?P<code>.*?)\n(?P=indent)(?P=fence)$", re.M | re.S)


def page_file(path):
    for ext in (".md", ".mdx"):
        if os.path.isfile(os.path.join(DOCS, path + ext)):
            return os.path.join(DOCS, path + ext)
    return None


def removed_upstream(docname):
    """A generated page of a platform no longer published in the registry."""
    if not mapping.is_generated(docname):
        return False
    parts = docname.split("/")
    platform = parts[1] if parts[0] == "boards" else parts[-1]
    if parts[0] == "frameworks":
        return False
    return page_file(mapping.map_docname("platforms/" + platform)) is None


def code_blocks(path):
    with open(path, encoding="utf-8") as fp:
        content = fp.read()
    blocks = collections.Counter()
    for match in FENCE_RE.finditer(content):
        indent = len(match.group("indent"))
        code = "\n".join(line[indent:] for line in match.group("code").split("\n"))
        blocks[code] += 1
    return blocks


def main():
    with open(REPORT) as fp:
        report = json.load(fp)
    errors = []
    dropped = {
        w.rsplit(": ", 1)[1]
        for w in report["warnings"]
        if "dropped list item linking to removed page" in w
    }

    pages = 0
    removed = []
    for docname, path in sorted(report["docs"].items()):
        if docname in mapping.SKIP or docname == mapping.HISTORY_DOCNAME:
            continue
        if mapping.is_partial(docname) and docname not in report["codeblocks"]:
            continue  # include-only fragment, rendered inside its parent
        if page_file(path) is None:
            if docname in dropped or removed_upstream(docname):
                removed.append(docname)
            else:
                errors.append("missing page: %s -> %s" % (docname, path))
            continue
        pages += 1

    blocks = 0
    for docname, expected in sorted(report["codeblocks"].items()):
        path = page_file(report["docs"][docname])
        if path is None:
            errors.append("missing page for code blocks: %s" % docname)
            continue
        actual = code_blocks(path)
        for code, count in collections.Counter(expected).items():
            blocks += count
            if actual[code] < count:
                errors.append(
                    "%s: code block differs or is missing:\n%s"
                    % (os.path.relpath(path, ROOT), code[:200])
                )

    for error in errors:
        print(error, file=sys.stderr)
    if removed:
        print("Not generated (removed from the registry): %s" % ", ".join(removed))
    print("Checked %d pages and %d code blocks: %d problems" % (pages, blocks, len(errors)))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

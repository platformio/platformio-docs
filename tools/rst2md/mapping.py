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

"""Maps legacy Sphinx docnames to document paths in the new structure.

A document path is relative to ``docs/`` and has no extension. The URL of a
document is ``/`` + its path, with a trailing ``/index`` removed.
"""

import re

# Docnames the converter does not write: the legacy root page is replaced by
# the new home page; the IDE features fragment is included by its parent
SKIP = {"index", "integration/ide/pioide_features"}
HISTORY_DOCNAME = "core/history"
SITE_URL = "https://docs.piolabs.com"

# Legacy deep links whose anchor moved to another page:
# (docname, anchor) -> (docname, anchor or None)
LEGACY_ANCHORS = {
    ("scripting/index", "before-pre-and-after-post-actions"): ("scripting/actions", None),
}

# Exact docname -> new path
EXACT = {
    "index": "index",
    "what-is-platformio": "get-started/what-is-platformio",
    "core/index": "get-started/platformio-core",
    "core/quickstart": "get-started/quick-start",
    "integration/ide/pioide": "get-started/platformio-ide",
    "integration/ide/pioide_features": "get-started/platformio-ide",
    "home/index": "get-started/platformio-home",
    "plus/pio-account": "get-started/platformio-account",
    "core/history": "resources/changelog",
    "core/migration": "resources/migration",
    "envvars": "reference/environment-variables",
    "projectconf/index": "reference/platformio-ini/index",
    "projectconf/build_configurations": "guides/projects/build-configurations",
    "projectconf/interpolation": "guides/projects/interpolation",
    "projectconf/examples": "guides/projects/examples",
    "projectconf/sections/env/index": "reference/platformio-ini/env/index",
    "projectconf/sections/platformio/index": "reference/platformio-ini/platformio/index",
    "plus/debugging": "guides/debugging/index",
    "plus/pio-remote": "guides/remote-development",
    "platforms/custom_platform_and_board": "guides/custom-platforms-and-boards/index",
    "platforms/creating_board": "guides/custom-platforms-and-boards/creating-board",
    "platforms/creating_platform": "guides/custom-platforms-and-boards/creating-platform",
    "platforms/index": "hardware/platforms/index",
    "frameworks/index": "hardware/frameworks/index",
    "boards/index": "hardware/boards/index",  # generated
    "integration/compile_commands": "guides/compile-commands",
    "core/userguide/index": "reference/cli/index",
    "scripting/actions": "reference/scripting-api/actions",
    "scripting/construction_environments": "reference/scripting-api/construction-environments",
    "scripting/middlewares": "reference/scripting-api/middlewares",
    "scripting/launch_types": "reference/scripting-api/launch-types",
    "scripting/index": "guides/scripting/index",
    "scripting/custom_targets": "guides/scripting/custom-targets",
}

# Ordered (regex, replacement) rules applied to the docname when it is not
# in EXACT. The replacement may use groups; path parts are slugified after.
RULES = [
    (r"^core/installation/(.+)$", r"get-started/install/\1"),
    (r"^tutorials/core/(.+)$", r"get-started/tutorials/\1"),
    (r"^tutorials/(.+)$", r"get-started/tutorials/\1"),
    (r"^librarymanager/(.+)$", r"guides/libraries/\1"),
    (r"^advanced/unit-testing/(.+)$", r"guides/unit-testing/\1"),
    (r"^advanced/static-code-analysis/(.+)$", r"guides/static-code-analysis/\1"),
    (r"^scripting/examples/(.+)$", r"guides/scripting/examples/\1"),
    (r"^integration/ide/(.+)$", r"guides/ide/\1"),
    (r"^integration/ci/(.+)$", r"guides/ci/\1"),
    # CLI: cmd_run -> pio-run, pkg/index -> pio-pkg/index, pkg/cmd_install -> pio-pkg/install
    (r"^core/userguide/cmd_(.+)$", r"reference/cli/pio-\1"),
    (r"^core/userguide/system/completion/index$", r"reference/cli/pio-system/completion/index"),
    (r"^core/userguide/system/completion/cmd_(.+)$", r"reference/cli/pio-system/completion/\1"),
    (r"^core/userguide/([^/]+)/index$", r"reference/cli/pio-\1/index"),
    (r"^core/userguide/([^/]+)/cmd_(.+)$", r"reference/cli/pio-\1/\2"),
    # platformio.ini: flat option pages, group pages as "<group>-options"
    (r"^projectconf/sections/(env|platformio)/options/([^/]+)/index$", r"reference/platformio-ini/\1/\2-options"),
    (r"^projectconf/sections/(env|platformio)/options/[^/]+/(.+)$", r"reference/platformio-ini/\1/\2"),
    (r"^manifests/library-json/index$", r"reference/library-json/index"),
    (r"^manifests/library-json/fields/(.+)$", r"reference/library-json/\1"),
    (r"^plus/debug-tools/(.+)$", r"hardware/debug-probes/\1"),
    (r"^faq/(.+)$", r"resources/faq/\1"),
    # Generated by scripts/docspregen.py (not written by the converter)
    (r"^boards/(.+)$", r"hardware/boards/\1"),
    (r"^platforms/(.+)$", r"hardware/platforms/\1"),
    (r"^frameworks/(.+)$", r"hardware/frameworks/\1"),
]

PARTIAL_RE = re.compile(r"^(platforms|frameworks|plus/debug-tools)/[^/]+(_extra|_debug)$")


def slugify(part):
    return part.lower().replace("_", "-").replace(".", "-")


def map_docname(docname):
    path = EXACT.get(docname)
    if path is None:
        for pattern, repl in RULES:
            if re.match(pattern, docname):
                path = re.sub(pattern, repl, docname)
                break
    if path is None:
        raise ValueError("No mapping for docname %r" % docname)
    parts = [slugify(p) for p in path.split("/")]
    if PARTIAL_RE.search(docname):
        # Partials are imported by generated pages; "_" hides them from routing
        parts[-1] = "_" + parts[-1]
    return "/".join(parts)


def is_generated(docname):
    """Pages fully written by scripts/docspregen.py."""
    if PARTIAL_RE.search(docname):
        return False
    if docname.startswith("boards/"):
        return True
    return bool(re.match(r"^(platforms|frameworks)/[^/]+$", docname)) and docname not in EXACT


def is_partial(docname):
    """Files meant to be included into another page, not standalone pages."""
    return bool(PARTIAL_RE.search(docname)) or docname.split("/")[-1].startswith("_")


def doc_url(path):
    url = "/" + path
    if url.endswith("/index"):
        url = url[: -len("/index")] or "/"
    return url or "/"

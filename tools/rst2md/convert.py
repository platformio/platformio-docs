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

"""Converts the legacy Sphinx/RST docs into Docusaurus Markdown in docs/.

Usage (from the docs repository root, with Sphinx installed):

    python tools/rst2md/convert.py

Files written by the previous run are removed first, so the conversion is
repeatable. Core's HISTORY.rst (included by the legacy changelog page) is
written as HISTORY.md next to it in the parent Core checkout. The run report is saved to tools/rst2md/out/report.json.
"""

import json
import os
import sys

from sphinx.cmd.build import build_main

HERE = os.path.dirname(os.path.realpath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
DOCS = os.path.join(ROOT, "docs")
OUT = os.path.join(HERE, "out")
REPORT = os.path.join(OUT, "report.json")


def clean_previous_run():
    if not os.path.isfile(REPORT):
        return
    with open(REPORT) as fp:
        report = json.load(fp)
    for path in report.get("written", []) + report.get("images", []):
        path = os.path.join(DOCS, path)
        if os.path.isfile(path):
            os.remove(path)
    for dirpath, dirnames, filenames in os.walk(DOCS, topdown=False):
        if dirpath != DOCS and not os.listdir(dirpath):
            os.rmdir(dirpath)


def main():
    clean_previous_run()
    return build_main(
        [
            "-b", "markdown",
            "-c", HERE,
            "-d", os.path.join(OUT, ".doctrees"),
            "-D", "md_outdir=%s" % DOCS,
            "-D", "md_history=%s" % os.path.join(os.path.dirname(ROOT), "HISTORY.md"),
            "-j", "auto",
            "-q",
            ROOT,
            OUT,
        ]
        + sys.argv[1:]
    )


if __name__ == "__main__":
    sys.exit(main())

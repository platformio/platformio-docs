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

import os
from string import Template


REDIRECT_TEMPLATE = Template(
    r"""
<!DOCTYPE html>
<html lang="en-US">
<head>
  <title>Redirecting...</title>
  <script>
    var redirect_url = "$redirect_url";
    if (window.location.search) {
      redirect_url += window.location.search;
    }
    if (window.location.hash) {
      redirect_url += window.location.hash;
    }
    window.location.href = redirect_url;
  </script>
  <link rel="canonical" href="$redirect_url" />
  <meta charset="utf-8" />
  <meta http-equiv="refresh" content="1; URL=$redirect_url" />
  <meta name="robots" content="noindex" />
</head>
<body>
  <h1>Redirecting...</h1>
  <p><a href="$redirect_url">Click here if you are not redirected.</a></p>
</body>
</html>
"""
)


def build_redirect_page(html_path, redirect_url):
    os.makedirs(os.path.dirname(html_path), exist_ok=True)
    with open(html_path, "w") as fp:
        fp.write(REDIRECT_TEMPLATE.substitute(redirect_url=redirect_url).strip())


def load_redirects(src_dir):
    redirects_txt = os.path.join(src_dir, "redirects.txt")
    assert os.path.isfile(redirects_txt)
    result = {}
    with open(redirects_txt) as fp:
        for line in fp.readlines():
            line = line.strip()
            skip_conds = [
                not line,
                not line.startswith("/"),
                "->" not in line,
            ]
            if any(skip_conds):
                continue
            from_path, to_path = line.split("->")
            from_path = from_path.strip()
            to_path = to_path.strip()
            assert from_path.endswith(".html")
            assert to_path.endswith(".html")
            result[from_path] = to_path
    return result


def build_redirect_pages(app, exception):
    if app.builder.name != "html":
        return
    is_latest = app.config.html_context.get("is_latest")
    redirects = load_redirects(app.srcdir)
    for from_path, to_path in redirects.items():
        out_dir = app.outdir
        if os.path.dirname(from_path) != "/":
            out_dir = os.path.join(out_dir, os.path.dirname(from_path)[1:])
        build_redirect_page(
            os.path.join(out_dir, os.path.basename(from_path)),
            "%s/en/%s/%s"
            % (
                app.config.html_baseurl,
                ("latest" if is_latest else "stable"),
                to_path,
            ),
        )

    print("Built %d redirect pages" % len(redirects))


def build_legacy_rtd_pages(app, exception):
    if app.builder.name != "html":
        return
    for root, dirs, files in os.walk(app.outdir):
        for name in files:
            if not name.endswith(".html"):
                continue
            out_dir = os.path.join(os.path.dirname(app.outdir), "rtdpage")
            relative_dir = root[len(os.path.commonpath([app.outdir, root])) :] or "/"
            if relative_dir != "/":
                out_dir = os.path.join(out_dir, relative_dir[1:])
            build_redirect_page(
                os.path.join(out_dir, name),
                "%s/en/latest%s/%s"
                % (
                    app.config.html_baseurl,
                    relative_dir,
                    name,
                ),
            )


def setup(app):
    app.connect("build-finished", build_redirect_pages)
    app.connect("build-finished", build_legacy_rtd_pages)
    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

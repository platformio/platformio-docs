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

"""Sphinx builder that writes the legacy RST docs as Docusaurus Markdown.

Sphinx parses and resolves the sources (``:ref:``, ``:option:``, includes,
substitutions, toctrees); this builder renders the resolved doctrees.
"""

import json
import os
import posixpath
import re
import shutil

from docutils import nodes
from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.util import logging

import mapping

logger = logging.getLogger(__name__)

DOC_URI_PREFIX = "@@doc/"

ADMONITIONS = {
    "note": ("note", None),
    "warning": ("warning", None),
    "caution": ("warning", None),
    "attention": ("warning", None),
    "danger": ("danger", None),
    "error": ("danger", None),
    "hint": ("tip", None),
    "tip": ("tip", None),
    "important": ("info", None),
    "seealso": ("info", "See also"),
}

LANGUAGES = {
    "default": "text",
    "none": "text",
    "text": "text",
    "console": "bash",
    "shell": "bash",
    "sh": "bash",
    "bash": "bash",
    "c++": "cpp",
    "js": "javascript",
    "cfg": "ini",
    "makefile": "makefile",
}

AUTO_ID_RE = re.compile(r"^(id|index-)\d+$")
MARKERS = ("begin_platforms",)
MARKER_IDS = {"debugging-platforms": "begin_platforms"}


class MarkdownBuilder(Builder):
    name = "markdown"
    format = "markdown"
    epilog = "Markdown written to %(outdir)s"
    allow_parallel = False

    def init(self):
        self.md_outdir = self.config.md_outdir
        self.report = {
            "docs": {},
            "written": [],
            "images": [],
            "codeblocks": {},
            "anchors": {},
            "warnings": [],
        }
        self.hosts = {}  # partial docname -> generated host docname
        self.top_ids = {}  # docname -> ids of its title section
        self.legacy_redirects = _load_legacy_redirects(self.srcdir)

    def get_outdated_docs(self):
        return self.env.found_docs

    def get_target_uri(self, docname, typ=None):
        return DOC_URI_PREFIX + docname

    def get_relative_uri(self, from_, to, typ=None):
        return self.get_target_uri(to, typ)

    def prepare_writing(self, docnames):
        for docname in self.env.found_docs:
            section = self.env.get_doctree(docname).next_node(nodes.section)
            if section is not None:
                self.top_ids[docname] = set(section.get("ids", []))
        for host, included in self.env.included.items():
            for docname in included:
                if mapping.is_generated(host) and mapping.is_partial(docname):
                    self.hosts[docname] = host
        # Labels defined in partials point to the generated page that
        # includes them, because the partial is rendered inside it
        std = self.env.domains.standard_domain
        for store in (std.labels, std.anonlabels):
            for name, value in list(store.items()):
                if value[0] in self.hosts:
                    store[name] = (self.hosts[value[0]],) + tuple(value[1:])

    def should_write(self, docname):
        if docname in mapping.SKIP or mapping.is_generated(docname):
            return False
        if mapping.is_partial(docname):
            return docname in self.hosts and self.generated_exists(self.hosts[docname])
        return True

    def generated_exists(self, docname):
        """Generated pages exist once scripts/docspregen.py has run; a legacy
        page it no longer produces (e.g. a platform dropped from the
        registry) does not."""
        path = os.path.join(self.md_outdir, mapping.map_docname(docname))
        return os.path.isfile(path + ".md") or os.path.isfile(path + ".mdx")

    def write_doc(self, docname, doctree):
        path = mapping.map_docname(docname)
        self.report["docs"][docname] = path
        if docname == mapping.HISTORY_DOCNAME:
            self.write_history(docname, path, doctree)
            return
        if not self.should_write(docname):
            return
        writer = MarkdownWriter(self, docname, path, doctree)
        content = writer.render()
        outfile = os.path.join(self.md_outdir, path + writer.extension)
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        self.report["written"].append(os.path.relpath(outfile, self.md_outdir))
        with open(outfile, "w", encoding="utf-8") as fp:
            fp.write(content)
        self.report["codeblocks"][docname] = writer.codeblocks
        self.report["anchors"][path] = sorted(writer.anchors)

    def write_history(self, docname, path, doctree):
        """Core's HISTORY.md: readable on GitHub, imported by the Changelog."""
        writer = MarkdownWriter(self, docname, path, doctree, standalone=True)
        content = writer.render()
        targets = [os.path.join(self.md_outdir, "resources", "_history.md")]
        if self.config.md_history:
            targets.append(self.config.md_history)
        for target in targets:
            with open(target, "w", encoding="utf-8") as fp:
                fp.write(content)

    def finish(self):
        for docname in self.env.found_docs:
            self.report["docs"].setdefault(docname, mapping.map_docname(docname))
        std = self.env.domains.standard_domain
        self.report["labels"] = {
            name: [self.report["docs"][docname], labelid]
            for name, (docname, labelid) in std.anonlabels.items()
            if docname in self.report["docs"]
        }
        os.makedirs(self.outdir, exist_ok=True)
        with open(os.path.join(self.outdir, "report.json"), "w") as fp:
            json.dump(self.report, fp, indent=2, sort_keys=True)


class MarkdownWriter:
    def __init__(self, builder, docname, path, doctree, standalone=False):
        self.builder = builder
        # Standalone output is read outside the site (GitHub): absolute links,
        # no Docusaurus-only heading id syntax
        self.standalone = standalone
        self.docname = docname
        self.path = path
        self.doctree = doctree
        self.partial = mapping.is_partial(docname)
        self.extension = ".md"
        self.codeblocks = []
        self.anchors = set()
        self.images = {}
        self.seen_title = False

    # -- helpers -----------------------------------------------------------

    def warn(self, message, node=None):
        line = getattr(node, "line", None) if node is not None else None
        self.builder.report["warnings"].append(
            "%s:%s: %s" % (self.docname, line or "?", message)
        )

    def link_to_doc(self, target_docname, anchor=None):
        target_docname, anchor = mapping.LEGACY_ANCHORS.get(
            (target_docname, anchor), (target_docname, anchor)
        )
        if anchor and anchor in self.builder.top_ids.get(target_docname, ()):
            anchor = None
        target = mapping.map_docname(target_docname)
        if self.standalone:
            return mapping.SITE_URL + mapping.doc_url(target) + ("#" + anchor if anchor else "")
        if mapping.is_generated(target_docname):
            url = mapping.doc_url(target)
        elif target == self.path and anchor:
            url = ""
        else:
            # Hand-written MDX pages (home, landing pages, changelog)
            mdx = os.path.join(self.builder.md_outdir, target + ".mdx")
            ext = ".mdx" if os.path.isfile(mdx) else ".md"
            url = posixpath.relpath(target + ext, posixpath.dirname(self.path) or ".")
            if not url.startswith("."):
                url = "./" + url
        if anchor:
            url += "#" + anchor
        return url

    def resolve_uri(self, refuri):
        if refuri.startswith(DOC_URI_PREFIX):
            target, _, anchor = refuri[len(DOC_URI_PREFIX):].partition("#")
            return self.link_to_doc(target, anchor or None)
        if refuri.startswith("#"):
            return refuri
        if not re.match(r"^[a-z][a-z0-9+.-]*:", refuri) and ".html" in refuri:
            # Raw relative link to a legacy page, e.g. "../ide/vscode.html#anchor"
            path, _, anchor = refuri.partition("#")
            old = posixpath.normpath(posixpath.join(posixpath.dirname(self.docname), path))
            old = old.removesuffix(".html")
            old = self.builder.legacy_redirects.get(old, old)
            if old in self.builder.env.found_docs:
                return self.link_to_doc(old, anchor or None)
            self.warn("unmapped relative link: %s" % refuri)
        match = re.match(r"^https?://docs\.platformio\.org/(?:en/[^/]+/)?(.*?)(?:\.html)?(#.*)?$", refuri)
        if match:
            old = re.sub(r"/+", "/", match.group(1) or "").strip("/") or "index"
            old = self.builder.legacy_redirects.get(old, old)
            if old in self.builder.env.found_docs or old + "/index" in self.builder.env.found_docs:
                docname = old if old in self.builder.env.found_docs else old + "/index"
                anchor = (match.group(2) or "")[1:] or None
                return self.link_to_doc(docname, anchor)
            self.warn("unmapped docs.platformio.org link: %s" % refuri)
        return refuri

    def copy_image(self, uri):
        if re.match(r"^[a-z]+://", uri):
            return uri
        src = os.path.join(self.builder.srcdir, uri)
        if not os.path.isfile(src):
            self.warn("missing image: %s" % uri)
            return uri
        if uri in self.images:
            return self.images[uri]
        page_dir = posixpath.dirname(self.path)
        name = os.path.basename(uri)
        dst_rel = posixpath.join(page_dir, "img", name)
        dst = os.path.join(self.builder.md_outdir, dst_rel)
        if os.path.isfile(dst) and not _same_file(src, dst):
            stem, ext = os.path.splitext(name)
            counter = 2
            while os.path.isfile(dst) and not _same_file(src, dst):
                name = "%s-%d%s" % (stem, counter, ext)
                dst_rel = posixpath.join(page_dir, "img", name)
                dst = os.path.join(self.builder.md_outdir, dst_rel)
                counter += 1
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        self.builder.report["images"].append(dst_rel)
        self.images[uri] = "./img/" + name
        return self.images[uri]

    def anchor_html(self, ids, tag="a"):
        out = []
        for id_ in ids:
            if AUTO_ID_RE.match(id_) or id_ in self.anchors:
                continue
            self.anchors.add(id_)
            out.append('<%s id="%s"></%s>' % (tag, id_, tag))
        return "".join(out)

    # -- document ----------------------------------------------------------

    def render(self):
        body = self.blocks(self.doctree.children, level=1 if self.partial else 0)
        body = body.strip() + "\n"
        return body

    # -- block rendering ---------------------------------------------------

    def blocks(self, children, level):
        out = []
        pending_ids = []
        for child in children:
            if isinstance(child, nodes.target) and not child.children:
                ids = child.get("ids", [])
                for id_ in ids + [child.get("refid", "")]:
                    if id_ in MARKER_IDS:
                        out.append("<!-- %s -->" % MARKER_IDS[id_])
                pending_ids.extend(ids)
                continue
            text = self.block(child, level)
            if pending_ids:
                anchors = self.anchor_html(pending_ids)
                pending_ids = []
                if anchors:
                    out.append(anchors)
            if text is not None and text.strip():
                out.append(text.strip("\n"))
        if pending_ids:
            anchors = self.anchor_html(pending_ids)
            if anchors:
                out.append(anchors)
        return "\n\n".join(out)

    def block(self, node, level):
        method = getattr(self, "block_" + node.__class__.__name__, None)
        if method:
            return method(node, level)
        if isinstance(node, nodes.Admonition):
            return self.admonition(node, level)
        if isinstance(node, (nodes.Invisible, nodes.substitution_definition)):
            return None
        if isinstance(node, nodes.Inline) or isinstance(node, nodes.Text):
            return self.inline_children([node])
        self.warn("unhandled block node <%s>" % node.tagname, node)
        return self.with_ids(node, self.blocks(node.children, level))

    def with_ids(self, node, text):
        anchors = self.anchor_html(node.get("ids", [])) if isinstance(node, nodes.Element) else ""
        if anchors:
            return anchors + "\n\n" + text if text else anchors
        return text

    def block_section(self, node, level):
        level += 1
        if level == 1:
            # Only the page title is a level-1 heading
            if self.seen_title:
                level = 2
            self.seen_title = True
        title = node.next_node(nodes.title)
        ids = list(node.get("ids", []))
        heading = "%s %s" % ("#" * min(level, 6), self.inline_children(title.children, heading=True))
        if self.standalone:
            # Only explicit labels; headings get their ids from the renderer
            title_id = nodes.make_id(title.astext())
            extra = self.anchor_html([i for i in ids if i != title_id])
        else:
            heading_id = _pick_heading_id(ids, title.astext())
            if heading_id and AUTO_ID_RE.match(heading_id):
                heading_id = None
            if heading_id:
                self.anchors.add(heading_id)
                heading += " {#%s}" % heading_id
            extra = self.anchor_html([i for i in ids if i != heading_id])
        parts = []
        if extra:
            parts.append(extra)
        parts.append(heading)
        rest = [c for c in node.children if c is not title]
        body = self.blocks(rest, level)
        if body:
            parts.append(body)
        return "\n\n".join(parts)

    def block_title(self, node, level):
        return "**%s**" % self.inline_children(node.children)

    block_rubric = block_title

    def block_paragraph(self, node, level):
        text = self.inline_children(node.children)
        text = _escape_line_start(text)
        return self.with_ids(node, text)

    def block_compact_paragraph(self, node, level):
        # Resolved toctrees wrap their bullet lists in a compact paragraph
        if any(isinstance(c, nodes.Body) and not isinstance(c, nodes.Inline) for c in node.children):
            return self.with_ids(node, self.blocks(node.children, level))
        return self.block_paragraph(node, level)

    def block_compound(self, node, level):
        return self.with_ids(node, self.blocks(node.children, level))

    def block_container(self, node, level):
        if node.get("literal_block"):
            caption = node.next_node(nodes.caption)
            code = node.next_node(nodes.literal_block)
            title = caption.astext() if caption is not None else None
            return self.with_ids(node, self.block_literal_block(code, level, title=title))
        return self.block_compound(node, level)

    block_div = block_compound

    def block_topic(self, node, level):
        if "contents" in node.get("classes", []):
            return None
        return self.with_ids(node, self.blocks(node.children, level))

    def block_comment(self, node, level):
        text = node.astext().strip()
        if text in MARKERS:
            return "<!-- %s -->" % text
        return None

    def block_transition(self, node, level):
        return "---"

    def block_raw(self, node, level):
        if node.get("format") == "html":
            return node.astext()
        return None

    def block_block_quote(self, node, level):
        # RST block quotes are indentation in these docs, not quotations
        return self.with_ids(node, self.blocks(node.children, level))

    def block_line_block(self, node, level):
        lines = []
        for line in node.traverse(nodes.line):
            lines.append(self.inline_children(line.children) or "")
        return self.with_ids(node, " \\\n".join(lines))

    def block_bullet_list(self, node, level):
        return self.with_ids(node, self.list_items(node, lambda i: "-", level))

    def block_enumerated_list(self, node, level):
        start = node.get("start", 1)
        return self.with_ids(node, self.list_items(node, lambda i: "%d." % (start + i), level))

    def list_items(self, node, marker, level):
        items = [c for c in node.children if isinstance(c, nodes.list_item)]
        rendered = []
        loose = False
        items = [i for i in items if not self.links_to_missing_page(i)]
        for index, item in enumerate(items):
            body = self.blocks(item.children, level)
            if "\n\n" in body:
                loose = True
            prefix = marker(index) + " "
            anchors = self.anchor_html(item.get("ids", []), tag="span")
            if anchors:
                body = anchors + body
            rendered.append(_indent_item(prefix, body))
        return ("\n\n" if loose else "\n").join(rendered)

    def links_to_missing_page(self, item):
        refs = list(item.traverse(nodes.reference))
        if len(refs) != 1 or not refs[0].get("refuri", "").startswith(DOC_URI_PREFIX):
            return False
        target = refs[0]["refuri"][len(DOC_URI_PREFIX):].partition("#")[0]
        if mapping.is_generated(target) and not self.builder.generated_exists(target):
            self.warn("dropped list item linking to removed page: %s" % target)
            return True
        return False

    def block_definition_list(self, node, level):
        out = []
        for item in node.children:
            if not isinstance(item, nodes.definition_list_item):
                continue
            terms = [c for c in item.children if isinstance(c, (nodes.term, nodes.classifier))]
            definition = item.next_node(nodes.definition)
            term = " : ".join(self.inline_children(t.children) for t in terms)
            anchors = self.anchor_html(item.get("ids", []) + sum((t.get("ids", []) for t in terms), []), tag="span")
            out.append("<dt>\n\n%s%s\n\n</dt>" % (anchors, term))
            if definition is not None:
                out.append("<dd>\n\n%s\n\n</dd>" % self.blocks(definition.children, level))
        return self.with_ids(node, "<dl>\n\n" + "\n\n".join(out) + "\n\n</dl>")

    def block_field_list(self, node, level):
        out = []
        for field in node.children:
            name = field.next_node(nodes.field_name)
            body = field.next_node(nodes.field_body)
            out.append("<dt>\n\n%s\n\n</dt>" % self.inline_children(name.children))
            out.append("<dd>\n\n%s\n\n</dd>" % self.blocks(body.children, level))
        return self.with_ids(node, "<dl>\n\n" + "\n\n".join(out) + "\n\n</dl>")

    def block_literal_block(self, node, level, title=None):
        code = node.astext()
        self.codeblocks.append(code)
        language = node.get("language")
        if not language:
            classes = [c for c in node.get("classes", []) if c not in ("code", "literal-block")]
            language = classes[0] if classes else "text"
        language = LANGUAGES.get(language.lower(), language.lower())
        meta = []
        if title:
            meta.append('title="%s"' % title.replace('"', "'"))
        hl_lines = node.get("highlight_args", {}).get("hl_lines")
        if hl_lines:
            meta.append("{%s}" % ",".join(str(n) for n in hl_lines))
        if node.get("linenos"):
            meta.append("showLineNumbers")
        fence = "```"
        while fence in code:
            fence += "`"
        info = " ".join([language] + meta)
        return self.with_ids(node, "%s%s\n%s\n%s" % (fence, info, code, fence))

    def block_doctest_block(self, node, level):
        return self.block_literal_block(node, level)

    def block_image(self, node, level):
        return self.with_ids(node, self.image(node))

    def block_figure(self, node, level):
        image = node.next_node(nodes.image)
        parts = [self.image(image)]
        caption = node.next_node(nodes.caption)
        if caption is not None:
            parts.append("*%s*" % self.inline_children(caption.children))
        legend = node.next_node(nodes.legend)
        if legend is not None:
            parts.append(self.blocks(legend.children, level))
        return self.with_ids(node, "\n\n".join(parts))

    def admonition(self, node, level):
        kind, default_title = ADMONITIONS.get(node.tagname, ("note", None))
        title = default_title
        children = list(node.children)
        if node.tagname == "admonition" and children and isinstance(children[0], nodes.title):
            title = self.inline_children(children[0].children)
            children = children[1:]
        body = self.blocks(children, level)
        fence = ":::"
        while re.search(r"^\s*%s" % re.escape(fence), body, re.M):
            fence += ":"
        head = fence + kind + ("[%s]" % title if title else "")
        return self.with_ids(node, "%s\n\n%s\n\n%s" % (head, body, fence))

    def block_versionmodified(self, node, level):
        body = self.blocks(node.children, level)
        if not body:
            body = self.inline_children(node.children)
        return ":::info\n\n%s\n\n:::" % body

    def block_seealso(self, node, level):
        return self.admonition(node, level)

    def block_table(self, node, level):
        title = node.next_node(nodes.title)
        tgroup = node.next_node(nodes.tgroup)
        thead = tgroup.next_node(nodes.thead)
        tbody = tgroup.next_node(nodes.tbody)
        head_rows = [r for r in thead.children if isinstance(r, nodes.row)] if thead else []
        body_rows = [r for r in tbody.children if isinstance(r, nodes.row)] if tbody else []
        caption = "**%s**\n\n" % self.inline_children(title.children) if title else ""
        table = self.gfm_table(head_rows, body_rows) or self.html_table(head_rows, body_rows, level)
        return self.with_ids(node, caption + table)

    def gfm_table(self, head_rows, body_rows):
        if len(head_rows) != 1:
            return None
        rows = []
        for row in head_rows + body_rows:
            cells = []
            for entry in row.children:
                if entry.get("morecols") or entry.get("morerows"):
                    return None
                if len(entry.children) > 1 or (
                    entry.children and not isinstance(entry.children[0], nodes.paragraph)
                ):
                    return None
                cell = self.inline_children(entry.children[0].children, table=True) if entry.children else ""
                anchors = self.anchor_html(entry.get("ids", []), tag="span")
                cells.append(anchors + cell)
            rows.append(cells)
        width = max(len(r) for r in rows)
        lines = []
        for index, cells in enumerate(rows):
            cells = cells + [""] * (width - len(cells))
            lines.append("| " + " | ".join(cells) + " |")
            if index == 0:
                lines.append("|" + "|".join(["---"] * width) + "|")
        return "\n".join(lines)

    def html_table(self, head_rows, body_rows, level):
        out = ["<table>"]
        for section, rows, tag in (("thead", head_rows, "th"), ("tbody", body_rows, "td")):
            if not rows:
                continue
            out.append("<%s>" % section)
            for row in rows:
                out.append("<tr>")
                for entry in row.children:
                    attrs = ""
                    if entry.get("morecols"):
                        attrs += ' colspan="%d"' % (entry["morecols"] + 1)
                    if entry.get("morerows"):
                        attrs += ' rowspan="%d"' % (entry["morerows"] + 1)
                    content = self.blocks(entry.children, level)
                    anchors = self.anchor_html(entry.get("ids", []), tag="span")
                    out.append("<%s%s>\n\n%s%s\n\n</%s>" % (tag, attrs, anchors, content, tag))
                out.append("</tr>")
            out.append("</%s>" % section)
        out.append("</table>")
        return "\n".join(out)

    # Sphinx object descriptions (.. option::, .. envvar::, .. py:class::)
    def block_desc(self, node, level):
        parts = []
        for child in node.children:
            if isinstance(child, addnodes.desc_signature):
                ids = list(child.get("ids", []))
                heading_id = ids[0] if ids else None
                if heading_id:
                    self.anchors.add(heading_id)
                extra = self.anchor_html(ids[1:])
                if extra:
                    parts.append(extra)
                text = "`%s`" % child.astext().replace("`", "")
                heading = "%s %s" % ("#" * min(level + 1, 6), text)
                if heading_id:
                    heading += " {#%s}" % heading_id
                parts.append(heading)
            elif isinstance(child, addnodes.desc_content):
                body = self.blocks(child.children, level + 1)
                if body:
                    parts.append(body)
        return "\n\n".join(parts)

    def block_index(self, node, level):
        return None

    def block_toctree(self, node, level):
        return None

    def block_only(self, node, level):
        return self.blocks(node.children, level)

    def block_footnote(self, node, level):
        label = node.next_node(nodes.label)
        rest = [c for c in node.children if not isinstance(c, nodes.label)]
        return self.with_ids(node, "%s. %s" % (label.astext() if label else "", self.blocks(rest, level)))

    def block_system_message(self, node, level):
        return None

    # -- inline rendering --------------------------------------------------

    def inline_children(self, children, heading=False, table=False):
        text = "".join(self.inline(c, table) for c in children)
        text = text.replace("\n", " ")
        if heading:
            text = text.strip()
        return text

    def inline(self, node, table=False):
        if isinstance(node, nodes.Text):
            return _escape(str(node), table)
        tag = node.__class__.__name__
        method = getattr(self, "inline_" + tag, None)
        if method:
            return method(node, table)
        if isinstance(node, (nodes.Invisible,)) or tag in ("index", "substitution_definition"):
            return ""
        return "".join(self.inline(c, table) for c in node.children)

    def _wrap(self, node, mark, table):
        inner = "".join(self.inline(c, table) for c in node.children)
        stripped = inner.strip()
        if not stripped:
            return inner
        lead = inner[: len(inner) - len(inner.lstrip())]
        trail = inner[len(inner.rstrip()):]
        return "%s%s%s%s%s" % (lead, mark, stripped, mark, trail)

    def inline_emphasis(self, node, table):
        return self._wrap(node, "*", table)

    inline_title_reference = inline_emphasis

    def inline_strong(self, node, table):
        return self._wrap(node, "**", table)

    def inline_literal(self, node, table):
        if "kbd" in node.get("classes", []):
            return "<kbd>%s</kbd>" % _escape(node.astext(), table)
        return _code_span(node.astext(), table)

    inline_literal_emphasis = inline_literal
    inline_literal_strong = inline_literal
    inline_desc_name = inline_literal

    def inline_inline(self, node, table):
        classes = node.get("classes", [])
        if "kbd" in classes:
            return "<kbd>%s</kbd>" % _escape(node.astext(), table)
        if "guilabel" in classes or "menuselection" in classes:
            return "**%s**" % _escape(node.astext(), table)
        return "".join(self.inline(c, table) for c in node.children)

    def inline_reference(self, node, table):
        image = node.next_node(nodes.image) if len(node.children) == 1 else None
        if image is not None and "_images/" in node.get("refuri", ""):
            # Sphinx links scaled images to their full-size copy
            return self.image(image)
        if "refuri" in node:
            url = self.resolve_uri(node["refuri"])
        elif "refid" in node:
            url = "#" + node["refid"]
        else:
            return "".join(self.inline(c, table) for c in node.children)
        if image is not None:
            label = self.image(image)
        else:
            label = "".join(self.inline(c, table) for c in node.children).strip()
        if not label:
            label = _escape(url, table)
        return "[%s](%s)" % (label, _escape_url(url))

    def inline_pending_xref(self, node, table):
        self.warn("unresolved reference: %s" % node.get("reftarget"), node)
        return "".join(self.inline(c, table) for c in node.children)

    def inline_target(self, node, table):
        anchors = self.anchor_html(node.get("ids", []), tag="span") if not node.get("refuri") else ""
        return anchors + "".join(self.inline(c, table) for c in node.children)

    def inline_image(self, node, table):
        return self.image(node)

    def inline_subscript(self, node, table):
        return "<sub>%s</sub>" % "".join(self.inline(c, table) for c in node.children)

    def inline_superscript(self, node, table):
        return "<sup>%s</sup>" % "".join(self.inline(c, table) for c in node.children)

    def inline_footnote_reference(self, node, table):
        return "<sup>[%s](#%s)</sup>" % (node.astext(), node.get("refid", ""))

    def inline_problematic(self, node, table):
        self.warn("problematic markup: %s" % node.astext(), node)
        return _escape(node.astext(), table)

    def inline_abbreviation(self, node, table):
        return _escape(node.astext(), table)

    def image(self, node):
        uri = node.get("uri", "")
        src = self.copy_image(uri)
        alt = _escape(node.get("alt", ""), False).replace("\n", " ")
        return "![%s](%s)" % (alt, _escape_url(src))


def _load_legacy_redirects(srcdir):
    """Old Sphinx redirects.txt: "/old.html -> /new.html" per line."""
    result = {}
    path = os.path.join(srcdir, "redirects.txt")
    if not os.path.isfile(path):
        return result
    with open(path) as fp:
        for line in fp:
            if "->" not in line:
                continue
            old, new = (p.strip().strip("/") for p in line.split("->"))
            result[old.removesuffix(".html")] = new.removesuffix(".html").split("#")[0]
    return result


def _same_file(a, b):
    with open(a, "rb") as fa, open(b, "rb") as fb:
        return fa.read() == fb.read()


def _pick_heading_id(ids, title):
    """Prefer the title-derived id, so headings keep their legacy anchor."""
    if not ids:
        return None
    title_id = nodes.make_id(title)
    if title_id in ids:
        return title_id
    for id_ in ids:
        if not AUTO_ID_RE.match(id_):
            return id_
    return ids[0]


def _escape(text, table=False):
    text = text.replace("\\", "\\\\")
    for char in "`*[]<~":
        text = text.replace(char, "\\" + char)
    text = re.sub(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])", r"\\_", text)
    text = re.sub(r"&(?=[A-Za-z0-9#]+;)", "&amp;", text)
    if table:
        text = text.replace("|", "\\|")
    return text


def _escape_line_start(text):
    if re.match(r"^(#|>|[-+*] |\d+[.)] |=+$|-+$|:::)", text):
        return "\\" + text
    return text


def _escape_url(url):
    return url.replace(" ", "%20").replace("(", "%28").replace(")", "%29")


def _code_span(text, table):
    text = text.replace("\n", " ")
    if table:
        text = text.replace("|", "\\|")
    fence = "`"
    while fence in text:
        fence += "`"
    if fence != "`" or text.startswith("`") or text.endswith("`"):
        return "%s %s %s" % (fence, text, fence)
    return "%s%s%s" % (fence, text, fence)


def _indent_item(prefix, body):
    pad = " " * len(prefix)
    lines = body.split("\n")
    out = [prefix + lines[0]]
    for line in lines[1:]:
        out.append(pad + line if line.strip() else "")
    return "\n".join(out)


def setup(app):
    app.add_config_value("md_outdir", "", "env")
    app.add_config_value("md_history", "", "env")
    app.add_builder(MarkdownBuilder)
    return {"parallel_read_safe": True, "parallel_write_safe": False}

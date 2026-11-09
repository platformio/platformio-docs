# PlatformIO Docs

Source of [https://docs.piolabs.com](https://docs.piolabs.com), built with
[Docusaurus](https://docusaurus.io/).

## Development

Requires Node.js (see `.nvmrc`).

```bash
npm ci
npm start          # live preview at http://localhost:3000
npm run build      # production build into build/
npm run typecheck
```

`npm start` and `npm run build` first copy PlatformIO Core's `HISTORY.md` for
the Changelog page: from the parent Core checkout when these docs are its
`docs/` submodule, otherwise from GitHub.

The build fails on broken links, anchors and Markdown links.

## Structure

| Path | Content |
| --- | --- |
| `docs/` | Pages. The folder layout is the URL layout. |
| `docs/hardware/` | Platforms, frameworks and boards, **generated** (see below) |
| `sidebars.ts` | Navigation: one sidebar per navbar area |
| `src/` | Theme customization and React components |
| `static/` | Fonts and images served as-is |
| `redirects.json` | Legacy (Sphinx) URLs mapped to the new pages |

Pages are Markdown (`.md`). Use `.mdx` only for pages that need React
components.

## Generated pages

The Hardware pages and the tail of the Debugging guide and debug probe pages
(after `<!-- begin_platforms -->`) are written by PlatformIO Core's
`scripts/docspregen.py`. Do not edit them by hand: their "Edit this page" link
points to the generator. Hand-written content of a platform or framework page
lives in its `_<name>-extra.md` / `_<name>-debug.md` partial.

From the PlatformIO Core repository:

```bash
cd scripts
python docspregen.py
```

## Hosting

The site uses `trailingSlash: false`: a page `/foo` is the file `foo.html`, and
a legacy redirect `/bar.html` is the file `bar.html.html`. Serve it with:

```nginx
location / {
    try_files $uri $uri.html $uri/ =404;
}
```

Legacy `docs.platformio.org` URLs are redirected by the pages listed in
`redirects.json`, once that domain forwards everything here:

```nginx
server {
    server_name docs.platformio.org;
    return 301 https://docs.piolabs.com$request_uri;
}
```

## Moving or removing a page

Add the page's old URL to the `from` list of its new target in
`redirects.json` (or a new `{"to": ..., "from": [...]}` entry), so links and
bookmarks keep working. A `from` path without `.html` covers the clean URL;
add the `.html` spelling as well for legacy Sphinx URLs.

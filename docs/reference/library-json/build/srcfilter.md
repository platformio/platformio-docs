---
description: "Specify which source files should be included/excluded from build process."
---

<a id="library-json-buid-src-filter"></a>

# `srcFilter` {#srcfilter}

- **Required:** No
- **Type:** String or array of strings

Specify which source files should be included/excluded from build process. The path in filter should be relative to the `srcDir` option of a library.

See syntax for [build_src_filter](../../platformio-ini/env/build-src-filter.md).

Note that you can generate source filter "on-the-fly" using `extraScript` (see below)

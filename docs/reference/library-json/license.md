---
description: "A SPDX license ID or SPDX Expression."
---

# `license`

- **Required:** No
- **Type:** String: an [SPDX license expression](https://spdx.org/licenses/)
- **Limits:** At most 255 characters.

A SPDX license ID or [SPDX Expression](https://spdx.github.io/spdx-spec/v3.0/annexes/SPDX-license-expressions/). You can check [the full list of SPDX license IDs](https://spdx.org/licenses/) (see "Identifier" column).

## Examples

A single license

```javascript
"license": "Apache-2.0"
```

Multiple license using SPDX Expression

```javascript
"license": "MIT AND (LGPL-2.1-or-later OR BSD-3-Clause)"
```

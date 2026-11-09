---
description: "A version of a current library source code."
---

<a id="manifest-library-json-version"></a>

# `version` {#version}

- **Required:** Yes
- **Type:** String
- **Limits:** At most 50 characters.

A version of a current library source code. Can contain a-z, digits, dots or dash and should be [Semantic Versioning](http://semver.org) compatible.

## Example

```javascript
"name": "Bar",
"version": "1.0.0",
"repository":
{
    "type": "git",
    "url": "https://github.com/foo/bar.git"
}
```

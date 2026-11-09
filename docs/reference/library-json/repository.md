---
description: "The repository in which the source code can be found."
---

# `repository`

- **Required:** No
- **Type:** Object

The repository in which the source code can be found. The field consists of the next items:

- `type` the only "git", "hg" or "svn" are supported
- `url`
- `branch` if is not specified, default branch will be used. This field will be ignored if tag/release exists with the value of [version](./version.md).

## Example

```javascript
"repository":
{
    "type": "git",
    "url": "https://github.com/foo/bar.git"
}
```

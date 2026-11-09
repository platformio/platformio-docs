---
description: "A list with compatible frameworks."
---

# `frameworks`

- **Required:** No
- **Type:** String or array of strings
- **Limits:** Each value: a framework name or `*`; at most 50 characters, only lowercase letters, digits, `-` and `_`.

A list with compatible frameworks. The available framework names are defined in the [Frameworks](../../hardware/frameworks/index.md) section.

## Example

```javascript
"frameworks": ["espidf", "freertos"]
```

If the library is compatible with the all frameworks, then do not declare this field or you use `*` symbol:

```javascript
"frameworks": "*"
```

# `frameworks` {#frameworks}

*Optional* | Type: `String` or `Array`

A list with compatible frameworks. The available framework names are defined in the [Frameworks](../../hardware/frameworks/index.md) section.

**Example**

```javascript
"frameworks": ["espidf", "freertos"]
```

If the library is compatible with the all frameworks, then do not declare this field or you use `*` symbol:

```javascript
"frameworks": "*"
```

# `include` {#include}

*Optional* | Type: `Array` | [Glob Pattern](http://en.wikipedia.org/wiki/Glob_%28programming%29)

Export only files that matched declared patterns.

**Pattern Meaning**

| Pattern | Meaning |
|---|---|
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in seq |
| `[!seq]` | matches any character not in seq |

**Example**

```javascript
"export": {
    "include":
    [
        "dir/*.[ch]pp",
        "dir/examples/*",
        "*/*/*.h"
    ]
}
```

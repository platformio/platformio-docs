---
description: "A list of header files that can be included in a project source files using #include <...> directive."
---

# `headers` {#headers}

- **Required:** No
- **Type:** String or array of strings
- **Limits:** Each header: at most 255 characters.

A list of header files that can be included in a project source files using `#include <...>` directive.

## Examples

```javascript
"headers": "MyLibrary.h"
```

```javascript
"headers": ["FooCore.h", "FooFeature.h"]
```

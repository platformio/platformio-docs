---
description: "A list of example patterns."
---

# `examples` {#examples}

- **Required:** No
- **Type:** Array
- **Values:** [glob patterns](http://en.wikipedia.org/wiki/Glob_%28programming%29)

A list of example patterns. This field is predefined with default value:

```javascript
"examples": [
    {
        "name": "Hello",
        "base": "examples/world",
        "files": [
            "platformio.ini",
            "include/world.h",
            "src/world.c",
            "README",
            "extra.py"
        ]
    },
    {
        "name": "Blink",
        "base": "examples/blink",
        "files": ["blink.cpp", "blink.h"]
    }
]
```

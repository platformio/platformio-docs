---
description: Convert an Arduino .ino sketch into a valid C++ file so that any editor can analyze it.
---

<a id="faq-convert-ino-to-cpp"></a>

# Convert an Arduino sketch to C++ {#convert-arduino-file-to-c-manually}

Arduino sketches (`.ino` and `.pde` files) are not valid C++: they rely on the
Arduino IDE to add `#include <Arduino.h>` and declarations of your functions.
Editors that do not support sketches therefore cannot offer code completion or
linting for them. Converting a sketch to a `.cpp` file fixes that.

For example, `Demo.ino`:

```cpp
void setup () {
    someFunction(13);
}

void loop() {
    delay(1000);
}

void someFunction(int num) {
}
```

To convert it to `Demo.cpp`:

1. Add `#include <Arduino.h>` at the top.
2. Declare each of your own functions before its first use. `setup()` and
   `loop()` do not need declarations.

The result:

```cpp
#include <Arduino.h>

void someFunction(int num);

void setup () {
    someFunction(13);
}

void loop() {
    delay(1000);
}

void someFunction(int num) {
}
```

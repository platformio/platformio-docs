<a id="faq-convert-ino-to-cpp"></a>

# Convert Arduino file to C++ manually {#convert-arduino-file-to-c-manually}

Some [Cloud & Desktop IDEs](../../guides/ide/index.md) don't support Arduino files (`*.ino` and `.pde`) because they are not valid C/C++ based source files:

1. Missing includes such as `#include <Arduino.h>`
2. Function declarations are omitted.

In this case, code completion and code linting do not work properly or are disabled. To avoid this issue you can manually convert your INO files to CPP.

For example, we have the next `Demo.ino` file:

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

Let's convert it to  `Demo.cpp`:

1. Add `#include <Arduino.h>` at the top of the source file
2. Declare each custom function (excluding built-in, such as `setup` and `loop`) before it will be called.

The final `Demo.cpp`:

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

Finish.

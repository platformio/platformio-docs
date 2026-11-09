# `builder` {#builder}

*Optional* | Type: `String`

Override default `PlatformIOLibBuilder` with another builder. Currently supported builders:

- `PlatformIOLibBuilder` (default)
- `ArduinoLibBuilder`
- `MbedLibBuilder`

## Examples {#examples}

1. Custom macros/defines

```javascript
"build": {
    "flags": "-D MYLIB_REV=1.2.3 -DRELEASE"
}
```

2. Extra includes for C preprocessor

```javascript
"build": {
    "flags": [
        "-I inc",
        "-I inc/target_x13"
    ]
}
```

3. Force to use `C99` standard instead of `C11`

```javascript
"build": {
    "unflags": "-std=gnu++11",
    "flags": "-std=c99"
}
```

4. Build source files (`c, cpp, h`) at the top level of the library

```javascript
"build": {
    "srcFilter": [
        "+<*.c>",
        "+<*.cpp>",
        "+<*.h>"
    ]
}
```

5. Extend PlatformIO Build System with own extra script

```javascript
"build": {
    "extraScript": "generate_headers.py"
}
```

`generate_headers.py`

```python
Import('env')
# print(env.Dump())
env.Append(
    CPPDEFINES=["HELLO=WORLD", "TAG=1.2.3", "DEBUG"],
    CPPPATH=["inc", "inc/devices"]
)

# some python code that generates header files "on-the-fly"
```

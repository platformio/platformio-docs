---
description: Show information about the PlatformIO Core installation.
---

<a id="cmd-system-info"></a>

# pio system info {#pio-system-info}

Show information about the PlatformIO Core installation: versions, paths,
encodings and the number of installed packages. Include it when you report a
problem.

## Usage {#usage}

```bash
pio system info [OPTIONS]
```

## Options {#options}

### `--json-output` {#cmdoption-pio-system-info-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

```bash
pio system info
```

```text
PlatformIO Core             5.0.0
Python                      3.8.5-final.0
System Type                 darwin_x86_64
Platform                    macOS-10.15.6
File System Encoding        utf-8
Locale Encoding             UTF-8
PlatformIO Core Directory   /Users/freedom/.platformio
PlatformIO Core Executable  /Users/freedom/.platformio/penv/bin/platformio
Python Executable           /Users/freedom/.platformio/penv/bin/python
Global Libraries            0
Development Platforms       37
Tools & Toolchains          79
```

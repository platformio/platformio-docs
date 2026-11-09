---
description: "An example with enabling specific checks and fixing code on the fly:."
---

<a id="check-tool-clangtidy"></a>

# Clang-Tidy {#clang-tidy}

**Clang-Tidy** is a clang-based C++ "linter" tool. Its purpose is to provide an extensible framework for diagnosing and fixing typical programming errors, like style violations, interface misuse, or bugs that can be deduced via static analysis. Official page can be found [here](https://clang.llvm.org/extra/clang-tidy).

## Features {#features}

**Clang-Tidy** supports a large variety of static checks that may not be covered by the compiler itself. These checks are static analysis checks that can be performed at a source code level.

Some of the defects that might be detected include:

- Buffer overflow
- Potential NULL pointer dereferences
- Use of memory that has already been deallocated
- Out of scope memory usage
- Failure to set a return value from a subroutine

## Configuration {#configuration}

To enable **Clang-Tidy** tool simply add it to the [check_tool](../../../reference/platformio-ini/env/check-tool.md) option in [`platformio.ini`](../../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
check_tool = clangtidy
```

Useful options that can be used used for adjusting check process:

- [Check options](../../../reference/platformio-ini/env/check-options.md)

  - [`check_tool`](../../../reference/platformio-ini/env/check-tool.md)
  - [`check_flags`](../../../reference/platformio-ini/env/check-flags.md)
  - [`check_severity`](../../../reference/platformio-ini/env/check-severity.md)
  - [`check_skip_packages`](../../../reference/platformio-ini/env/check-skip-packages.md)
  - [`check_src_filters`](../../../reference/platformio-ini/env/check-src-filters.md)

## Supported checks {#supported-checks}

There are currently the following groups of most used checks (By default all checks are enabled):

| Check | Description |
|---|---|
| `abseil-` | Checks related to Abseil library. |
| `boost-` | Checks related to Boost library. |
| `bugprone-` | Checks that target bugprone code constructs. |
| `cert-` | Checks related to CERT Secure Coding Guidelines. |
| `cppcoreguidelines-` | Checks related to C++ Core Guidelines. |
| `clang-analyzer-` | Clang Static Analyzer checks. |
| `google-` | Checks related to Google coding conventions. |
| `hicpp-` | Checks related to High Integrity C++ Coding Standard. |
| `modernize-` | Checks that advocate usage of modern (currently modern means `C++11`) language constructs. |
| `performance-` | Checks that target performance-related issues. |
| `portability-` | Checks that target portability-related issues that don’t relate to any particular coding style. |
| `readability-` | Checks that target readability-related issues that don’t relate to any particular coding style. |

The full list of supported checks can be found on [the official webpage](https://clang.llvm.org/extra/clang-tidy/checks/list.html).

## Extra flags {#extra-flags}

Useful flags that can help more precisely configure **Clang-Tidy** to satisfy your project requirements:

| Flag | Meaning |
|---|---|
| `--checks=<string>` | Comma-separated list of enabled checks (`*` default) |
| `--fix` | Apply suggested fixes. Without `-fix-errors` clang-tidy will bail out if any compilation errors were found. |
| `--fix-errors` | Apply suggested fixes even if compilation errors were found. If compiler errors have attached fix-its, clang-tidy will apply them as well. |
| `--format-style=<string>` | Style for formatting code around applied fixes: `llvm`, `google`, `webkit`, `mozilla`, `none (default)` |
| `--system-headers` | Display the errors from system headers |
| `--config-file=<path>` | Specify the path of `.clang-tidy` or custom config file. |

An example with enabling specific checks and fixing code on the fly:

```ini
[env:myenv]
platform = ...
board = ...
check_tool = clangtidy
check_flags =
  clangtidy: --checks=-*,cert-*,clang-analyzer-* --fix
```

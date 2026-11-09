---
description: "In order to use the CERT addon, simply specify it as an additional flag in check_flags section:."
---

# Cppcheck

**Cppcheck** is a static analysis tool for C/C++ code. It provides a unique code analysis to detect bugs and focuses on detecting undefined behavior and dangerous coding constructs. The goal is to detect only real errors in the code (i.e. have very few false positives). More information about this tool on [the official webpage](http://cppcheck.sourceforge.net).

:::tip

Cppcheck is rarely wrong about reported errors. But there are many bugs that it doesn't detect. You will find more bugs in your software by testing your software carefully than by using Cppcheck.

:::

## Features {#features}

**Cppcheck** supports a wide variety of static checks that may not be covered by the compiler itself. These checks are static analysis checks that can be performed at a source code level. The program is directed towards static analysis checks that are rigorous, rather than heuristic in nature.

<dl>

<dt>

Some of the defects that might be detected include:

</dt>

<dd>

- Automatic variable checking
- Bounds checking for array overruns
- Classes checking (e.g. unused functions, variable initialization, and memory duplication)
- Usage of deprecated or superseded functions
- Exception safety checking, for example, usage of memory allocation and destructor checks
- Memory leaks, e.g. due to lost scope without deallocation
- Resource leaks, e.g. due to forgetting to close a file handle
- Invalid usage of Standard Template Library functions and idioms
- Miscellaneous stylistic and performance errors

</dd>

</dl>

## Additional checks {#additional-checks}

Be default **Cppcheck** is configured to check the next additional defects:

- `warning`
- `style`
- `performance`
- `portability`
- `unusedFunction`

The full list of supported check with detailed description is located on [the official webpage](https://sourceforge.net/p/cppcheck/wiki/ListOfChecks/).

## Configuration {#configuration}

**Cppcheck** is implicitly used as the default check tool when [check_tool](../../../reference/platformio-ini/env/check-tool.md) option in [`platformio.ini`](../../../reference/platformio-ini/index.md) is not set. To be explicit, you can specify it in the configuration directly:

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck
check_flags = --enable=all
```

Useful options that can be used used for adjusting check process:

- [Check options](../../../reference/platformio-ini/env/check-options.md)

  - [`check_tool`](../../../reference/platformio-ini/env/check-tool.md)
  - [`check_flags`](../../../reference/platformio-ini/env/check-flags.md)
  - [`check_severity`](../../../reference/platformio-ini/env/check-severity.md)
  - [`check_skip_packages`](../../../reference/platformio-ini/env/check-skip-packages.md)
  - [`check_src_filters`](../../../reference/platformio-ini/env/check-src-filters.md)

## Extra flags {#extra-flags}

Useful flags that can help more precisely configure **Cppcheck** to satisfy your project requirements:

| Flag | Meaning |
|---|---|
| `--enable=<id>` | Enable additional checks. The available ids are: `all`, `warning`, `style`, `performance`, `portability`, `information`, `unusedFunction`, `missingInclude` |
| `--std=<id>` | Set standard. The available options are: `c89`, `c99`, `c11`, `c++03`, `c++11`, `c++14`, `c++17`, `c++20 (default)` |
| `--language=<language>` | Forces **Cppcheck** to check all files as the given language. Valid values are: `c`, `c++` |
| `--inline-suppr` | Enable inline suppressions. Use them by placing one or more comments, like: `// cppcheck-suppress warningId` on the lines before the warning to suppress (enabled by default if no extra flags specified). |
| `--suppress=<spec>` | Suppress warnings that match `<spec>`. The format of `<spec>` is: `[error id]:[filename]:[line]` |
| `--platform=<type>` | Specifies platform-specific types and sizes. The available built-in platforms are: `unix32`, `unix64`, `win32A`, `win32W`, `win64`, `avr8`, `native`, `unspecified (default)` |
| `--inconclusive` | Allow reporting defects even though the analysis is inconclusive. |
| `-D<ID>` | Define a preprocessor symbol. Example: `-DDEBUG=1` |
| `-U<ID>` | Undefine preprocessor symbol. Use -U to explicitly hide certain #ifdef \<ID> code paths from checking. Example: `-UDEBUG` |
| `-I <dir>` | Give a path to search for include files. Give several -I parameters to give several paths. |
| `-j <jobs>` | Start `<jobs>` threads to do the checking simultaneously. |

## Suppressing warnings {#suppressing-warnings}

It might be useful to explicitly instruct **Cppcheck** to ignore some of the known defects in project codebase. Since `--inline-suppr` is enabled by default, it's possible to directly mark pieces of code that will be excluded from **Cppcheck** report using `// cppcheck-suppress warningId` syntax.

:::note

Warning ID can be found in square brackets at the end of defect description, for example: `src\Blink.cpp:17: [low:style] The function 'loop' is never used. [unusedFunction]`

:::

By default, [Static Code Analysis](../index.md) command doesn't scan framework sources and that's why some functions from in your project might be reported as unused. For example, you can ignore warnings about `setup` and `loop` functions from Arduino-based projects:

```c
// cppcheck-suppress unusedFunction
void setup()
{
  ...
}

// cppcheck-suppress unusedFunction
void loop()
{
  ...
}
```

## Addons (MISRA, CERT) {#addons-misra-cert}

**Cppcheck** provides several addon scripts that analyze dump files to check compatibility with secure coding standards and to locate various issues. Most useful addons for verifying compliance with popular guidelines are **MISRA** and **CERT**.

### MISRA {#misra}

`MISRA` is a proprietary set of software development guidelines for the C/C++ programming languages developed by MISRA (Motor Industry Software Reliability Association).  It aims to facilitate code safety, security, portability, and reliability  in the context of embedded systems, specifically those systems programmed in ISO C/C++.

:::note

Since this standard is proprietary, **Cppcheck** does not display error text by specifying only the number of violated rules (for example, \[c2012-21.3\]). If you want to display full texts for violated rules, you will need to create a text file containing MISRA rules, which you will have to pass when calling the script with `--rule-texts` flag.

:::

In order to use `MISRA` addon you will need to provide a special file with the description of `MISRA` rules. Usually, it has the next contents:

```ini
Appendix A Summary of guidelines
Rule 3.1 Required
R3.1 Rule description
Rule 4.1 Required
...
Rule 21.3 Required
R21.3 Rule description
Rule 21.4
R21.4 Rule description
```

Next, you need to instruct **Cppcheck** that you want to run an additional addon script. Since this script requires an additional file with rules, you can pass it via a special `json` file:

```json
{
  "script": "addons/misra.py",
  "args": ["--rule-texts=misra-rules.txt"]
}
```

Finally, add new flag to [check_flags](../../../reference/platformio-ini/env/check-flags.md):

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck
check_flags =
  cppcheck: --addon=misra.json
```

The full list of implemented `MISRA` checks can be found on [the official webpage](http://cppcheck.sourceforge.net/misra.php).

### CERT {#cert}

`SEI CERT` coding standard provides rules for secure coding in the C programming language. The goal of these rules and recommendations is to develop safe, reliable, and secure systems, for example by eliminating undefined behaviors that can lead to undefined program behaviors and exploitable vulnerabilities.

In order to use the `CERT` addon, simply specify it as an additional flag in [check_flags](../../../reference/platformio-ini/env/check-flags.md) section:

```ini
[env:myenv]
platform = ...
board = ...
check_tool = cppcheck
check_flags =
  cppcheck: --addon=cert.py
```

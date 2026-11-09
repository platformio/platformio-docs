---
description: "A pattern to determine when debugging server is ready for an incoming connection (platformio.ini option debug_server_ready_pattern)."
---

# `debug_server_ready_pattern` {#debug-server-ready-pattern}

- **Type:** String
- **Multiple values:** No

A pattern to determine when debugging server is ready for an incoming connection. The pattern applies tool debugging server process's STDOUT and STDERR outputs.

A regular expression (RegExp) is allowed if the pattern starts with `-` character. See [Python regular expression operations](https://docs.python.org/3/library/re.html) for syntax and details.

## Examples

```ini
[env:custom_debug_server_ready_pattern]
...

; match by string
debug_server_ready_pattern = Waiting for GDB connection

; match by regular expression
debug_server_ready_pattern = -.*Listening on port \d+ for gdb connections
```

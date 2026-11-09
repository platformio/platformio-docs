# `name` {#name}

**Required** | Type: `String` | Max. Length: 50

A name of a library.

- Must be unique in the [PlatformIO Registry](https://registry.platformio.org)
- Should be slug style for simplicity, consistency, and compatibility. Example: *HelloWorld*
- Can contain a-z, digits, and dashes (but not start/end with them)
- Consecutive dashes and \[:;/,@\<>\] chars are not allowed.

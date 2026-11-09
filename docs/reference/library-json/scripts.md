---
description: "Execute custom scripts during the special Package Management CLI life cycle events."
---

# `scripts`

- **Required:** No
- **Type:** Object with `postinstall` and `preuninstall` keys

Execute custom scripts during the special [Package Management CLI](../cli/pio-pkg/index.md) life cycle events:

| Event | Description |
|---|---|
| `postinstall` | runs a script AFTER the package has been installed |
| `preuninstall` | runs a script BEFORE the package is removed. |

:::note

Both `postinstall` and `preuninstall` values must be specified as a *list* (array). Even if you need to run a single command, provide it as a one-item list. Each list contains the command (executable) as the first element and optional arguments as subsequent elements.

:::

## Examples

1. Run a custom Python script located in the package "scripts" folder AFTER the package is installed. Note that you don't need to specify a Python interpreter for Python scripts.

   ```javascript
   "scripts": {
       "postinstall": ["scripts/after_install.py"]
   }
   ```

2. Run a custom Bash script BEFORE the package is uninstalled. The script is declared as a list of command arguments and is located at the root of a package:

   ```javascript
   "scripts": {
       "preuninstall": ["maintenance.sh", "--action", "uninstall"]
   }
   ```

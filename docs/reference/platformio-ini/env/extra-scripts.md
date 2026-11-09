---
description: "A list of PRE and POST extra scripts (platformio.ini option extra_scripts)."
---

<a id="projectconf-extra-scripts"></a>

# `extra_scripts` {#extra-scripts}

- **Type:** String
- **Multiple values:** Yes
- **Environment variable:** [`PLATFORMIO_EXTRA_SCRIPTS`](../../environment-variables.md#envvar-PLATFORMIO_EXTRA_SCRIPTS), appended to the values in `platformio.ini`
- **Deprecated name:** `extra_script` (still accepted, with a warning)

A list of PRE and POST extra scripts. Paths are relative to the project folder. See details and examples in the [Advanced Scripting](../../../guides/scripting/index.md) and [Launch Types](../../scripting-api/launch-types.md) sections.

If you plan to share these scripts with [Remote Development](../../../guides/remote-development.md) machine, please put them to [shared_dir](../platformio/shared-dir.md).

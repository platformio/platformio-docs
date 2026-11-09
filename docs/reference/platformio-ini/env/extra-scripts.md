<a id="projectconf-extra-scripts"></a>

# `extra_scripts` {#extra-scripts}

Type: `FilePath` | Multiple: `Yes`

A list of PRE and POST extra scripts. Paths are relative to the project folder. See details and examples in the [Advanced Scripting](../../../guides/scripting/index.md) and [Launch Types](../../scripting-api/launch-types.md) sections.

If you plan to share these scripts with [Remote Development](../../../guides/remote-development.md) machine, please put them to [shared_dir](../platformio/shared-dir.md).

This option can also be set by the global environment variable [`PLATFORMIO_EXTRA_SCRIPTS`](../../environment-variables.md#envvar-PLATFORMIO_EXTRA_SCRIPTS).

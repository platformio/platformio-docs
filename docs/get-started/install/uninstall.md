---
description: Remove PlatformIO Core and the packages it installed.
---

<a id="piocore-uninstall"></a>

# Uninstall PlatformIO Core {#uninstall-platformio-core-and-dependent-packages}

PlatformIO Core keeps itself (when installed with the
[installer script](./installer-script.md)), its packages, platforms,
toolchains and settings in
[`core_dir`](../../reference/platformio-ini/platformio/core-dir.md):
`~/.platformio` by default, or `%USERPROFILE%\.platformio` on Windows.

To uninstall:

1. If you installed PlatformIO Core with [pip](./pip.md) or
   [Homebrew](./homebrew.md), remove it with the same tool:

   ```bash
   python -m pip uninstall platformio

   # or, if you used Homebrew
   brew uninstall platformio
   ```

2. Delete the `core_dir` folder.

3. If you [installed the shell commands](./shell-commands.md), remove the
   links or the `Path` entry you added.

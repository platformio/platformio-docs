<a id="piocore-uninstall"></a>

# Uninstall PlatformIO Core and dependent packages {#uninstall-platformio-core-and-dependent-packages}

- The isolated installation of PlatformIO Core and dependent packages are installed to the [core_dir](../../reference/platformio-ini/platformio/core-dir.md) folder. Just remove it.

- Uninstall global PlatformIO Core if you did not use the [Installer Script (Recommended)](./methods/installer-script.md):

  ```bash
  # uninstall standalone PlatformIO Core installed via `pip`
  pip uninstall platformio
  python -m pip uninstall platformio

  # uninstall Homebrew's PlatformIO Core (only macOS users if you installed it via Homebrew before)
  brew uninstall platformio
  ```

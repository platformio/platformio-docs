<a id="installation-pypi"></a>

# Python Package Manager {#python-package-manager}

:::warning

It's best to stick with this method **ONLY IF** you're dealing with [Continuous Integration](../../../guides/ci/index.md) systems/containers or if you have complete permissions to set up PlatformIO Core across your entire operating system.

For your own personal use, and to steer clear of troubles when it comes to maintenance and updates, we **STRONGLY SUGGEST** going for the [Installer Script (Recommended)](./installer-script.md). This script installs PlatformIO Core in a separate virtual environment, keeping it isolated from your operating system and avoiding any impact on it.

:::

The latest stable version of PlatformIO Core may be installed or upgraded via Python Package Manager ([pip](https://pip.pypa.io)) as follows:

```bash
python3 -m pip install -U platformio
```

---
description: Upgrade PlatformIO Core to the latest version.
---

<a id="cmd-upgrade"></a>

# pio upgrade {#pio-upgrade}

Check for a newer version of PlatformIO Core and upgrade to it.

## Usage {#usage}

```bash
pio upgrade [OPTIONS]
```

## Options {#options}

### `--dev` {#cmdoption-pio-upgrade-dev}

Upgrade to the [development version](../../get-started/install/development-version.md)
from the `develop` branch.

### `--only-dependencies` {#cmdoption-pio-upgrade-only-dependencies}

Upgrade only the Python packages that PlatformIO Core depends on, not
PlatformIO Core itself.

### `-v, --verbose` {#cmdoption-pio-upgrade-verbose}

Print the output of the underlying `pip` commands.

## Examples {#examples}

```bash
pio upgrade
```

```text
You are up-to-date!
PlatformIO x.x.x is currently the newest version available.
```

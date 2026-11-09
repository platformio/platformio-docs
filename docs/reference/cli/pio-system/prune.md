---
description: Free disk space by removing cached data and unused PlatformIO packages.
---

# pio system prune

Free disk space by removing data PlatformIO no longer needs.

## Usage {#usage}

```bash
pio system prune [OPTIONS]
```

## Description {#description}

The command removes, after asking for confirmation:

- cached API requests and package downloads, and temporary data;
- core packages that PlatformIO Core no longer uses;
- packages of development platforms that no installed platform uses.

PlatformIO reminds you to run it when the unused data exceeds the
[`check_prune_system_threshold`](../pio-settings.md#setting-check-prune-system-threshold)
setting.

:::tip

To keep a custom package in
[`packages_dir`](../../platformio-ini/platformio/packages-dir.md), create an
empty `.piokeep` file in the package's root folder.

:::

## Options {#options}

<a id="cmdoption-pio-system-prune-f"></a>

### `-f, --force` {#cmdoption-pio-system-prune-force}

Do not ask for confirmation.

### `--dry-run` {#cmdoption-pio-system-prune-dry-run}

Only show what would be removed.

### `--cache` {#cmdoption-pio-system-prune-cache}

Remove only cached data.

### `--core-packages` {#cmdoption-pio-system-prune-core-packages}

Remove only unused core packages.

### `--platform-packages` {#cmdoption-pio-system-prune-platform-packages}

Remove only unused development platform packages.

## Examples {#examples}

```bash
pio system prune
```

```text
Prune cached data:
 - cached API requests
 - cached package downloads
 - temporary data
Do you want to continue? [y/N]: y
Space on disk: 2.34MB

Prune unnecessary core packages:
Calculating...
Do you want to continue? [y/N]: y
Space on disk: 0B

Prune unnecessary development platform packages:
Calculating...
Package                                 Version       Size
--------------------------------------  ------------  --------
platformio/framework-stm32cube          2.0.200813    458.88MB
platformio/framework-arduinosam         4.4.191002    290.35MB
platformio/framework-arduino-samd       1.8.9         17.59MB
platformio/framework-arduinonordicnrf5  1.600.190830  4.70MB
Do you want to continue? [y/N]: y
Tool Manager: Removing framework-arduino-samd @ 1.8.9
Tool Manager: framework-arduino-samd @ 1.8.9 has been removed!
Tool Manager: Removing framework-arduinonordicnrf5 @ 1.600.190830
Tool Manager: framework-arduinonordicnrf5 @ 1.600.190830 has been removed!
Tool Manager: Removing framework-arduinosam @ 4.4.191002
Tool Manager: framework-arduinosam @ 4.4.191002 has been removed!
Tool Manager: Removing framework-stm32cube @ 2.0.200813
Tool Manager: framework-stm32cube @ 2.0.200813 has been removed!
Space on disk: 771.52MB

Total reclaimed space: 773.86MB
```

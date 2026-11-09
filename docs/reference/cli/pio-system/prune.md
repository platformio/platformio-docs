<a id="cmd-system-prune"></a>

# pio system prune {#pio-system-prune}

## Usage {#usage}

```bash
pio system prune
```

## Description {#description}

Remove unused data:

- cached API requests
- cached package downloads
- temporary data
- unnecessary core packages
- unnecessary development platform packages.

:::note

If you have a custom package in [packages_dir](../../platformio-ini/platformio/packages-dir.md) folder and would like to skip it from "prune process", please add empty `.piokeep` file to the root of a package folder.

:::

## Options {#options}

<a id="cmdoption-pio-system-prune-f"></a>

### `--force, -f` {#cmdoption-pio-system-prune-force}

Do not prompt for confirmation.

### `--dry-run` {#cmdoption-pio-system-prune-dry-run}

Do not prune, only show data that will be removed.

### `--cache` {#cmdoption-pio-system-prune-cache}

Prune only cached data.

### `--core-packages` {#cmdoption-pio-system-prune-core-packages}

Prune only unnecessary core packages.

### `--platform-packages` {#cmdoption-pio-system-prune-platform-packages}

Prune only unnecessary development platform packages.

## Examples {#examples}

```text
> pio system prune

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

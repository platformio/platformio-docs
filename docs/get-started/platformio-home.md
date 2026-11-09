---
description: PlatformIO Home is the graphical interface for projects, libraries, platforms, boards and devices.
---

# PlatformIO Home

PlatformIO Home is a graphical interface for PlatformIO that runs in a web
browser or inside [PlatformIO IDE](./platformio-ide.md). Use it to:

- Create, import and open projects.
- Search, install and update [libraries](../guides/libraries/index.md).
- Browse and manage [development platforms](../hardware/platforms/index.md),
  [frameworks](../hardware/frameworks/index.md) and [boards](/hardware/boards).
- List connected [devices](../reference/cli/pio-device/index.md): serial ports,
  logical drives and multicast DNS services.
- Inspect a project: memory usage, firmware sections and symbols, and
  [static code analysis](../guides/static-code-analysis/index.md) results.
- Manage your [PlatformIO Account](./platformio-account.md).

PlatformIO Home is part of PlatformIO IDE and PlatformIO Core; there is
nothing extra to install.

## Open PlatformIO Home {#quick-start}

<a id="platformio-ide"></a>

**In PlatformIO IDE for VS Code**, select the **Home** button on the
[PlatformIO toolbar](../guides/ide/vscode.md#platformio-toolbar).

<a id="platformio-core"></a>

**From the command line**, start the PlatformIO Home server with
[`pio home`](../reference/cli/pio-home.md):

```bash
pio home
```

It opens [http://127.0.0.1:8008](http://127.0.0.1:8008) in your browser. To
use another host or port, see the [`pio home` options](../reference/cli/pio-home.md).

## Screens {#demo}

### Welcome and projects {#welcome-project-manager}

![PlatformIO Home welcome screen with recent projects](./img/pio-home-welcome.png)

### Project inspection {#project-inspect}

#### Statistics {#statistics}

Memory usage and code statistics of the built firmware:

![Project inspection statistics](./img/pio-home-inspect-stats.png)

When you run only the code analysis:

![Project inspection with code analysis only](./img/pio-home-inspect-stats-check.png)

#### Firmware file explorer {#firmware-file-explorer}

![Firmware file explorer](./img/pio-home-inspect-firmware-file-explorer.png)

Symbols of a selected file:

![Firmware file explorer with file symbols](./img/pio-home-inspect-firmware-file-explorer-symbols.png)

#### Firmware symbols {#firmware-symbols}

![Firmware symbols](./img/pio-home-inspect-firmware-symbols.png)

#### Firmware sections {#firmware-sections}

![Firmware sections](./img/pio-home-inspect-firmware-sections.png)

#### Code defects {#static-code-analysis}

Results of [static code analysis](../guides/static-code-analysis/index.md):

![Code defects found by static analysis](./img/pio-home-inspect-code-defects.png)

### Libraries {#library-manager}

![Library manager](./img/pio-home-library-stats.png)

### Boards {#board-explorer}

![Board explorer](./img/pio-home-boards.png)

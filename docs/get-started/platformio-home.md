<a id="piohome"></a>

# PlatformIO Home {#platformio-home}

**PlatformIO Home** is a powerful, modern, and interactive user interface (UI) for PlatformIO collaborative platform. It's powered by [PlatformIO Labs's Modern UI Toolkit](https://piolabs.com/technology/modern-ui-toolkit.html) and contains the following key instruments:

- [PlatformIO Account](./platformio-account.md)
- Project Management
- [Library Management](../guides/libraries/index.md)
- [Development Platforms](../hardware/platforms/index.md), [Frameworks](../hardware/frameworks/index.md), and [Boards](/hardware/boards) Management
- [Device Management](../reference/cli/pio-device/index.md) (serial, logical, and multicast DNS services)
- Static Code Analysis
- Firmware File Explorer
- Firmware Memory Inspection
- Firmware Sections & Symbols Viewer.

## Installation {#installation}

You do not need to install **PlatformIO Home** separately, it's already built-in in [PlatformIO IDE](./platformio-ide.md) and [PlatformIO Core (CLI)](./platformio-core.md).

## Quick Start {#quick-start}

### PlatformIO IDE {#platformio-ide}

Please open **PlatformIO Home** using (HOME) button on PlatformIO Toolbar:

- **VSCode**: [PlatformIO Toolbar](../guides/ide/vscode.md#ide-vscode-toolbar)

### PlatformIO Core {#platformio-core}

Please launch **PlatformIO Home** Web-server using [pio home](../reference/cli/pio-home.md) command and open in your browser [http://127.0.0.1:8008](http://127.0.0.1:8008).

You can change host and port. Please check [pio home](../reference/cli/pio-home.md) command for details.

## Demo {#demo}

### Welcome & Project Manager {#welcome-project-manager}

![](./img/pio-home-welcome.png)

### Project Inspect {#project-inspect}

#### Statistics {#statistics}

![](./img/pio-home-inspect-stats.png)

Only code analysis ([Static Code Analysis](../guides/static-code-analysis/index.md))

![](./img/pio-home-inspect-stats-check.png)

#### Firmware File Explorer {#firmware-file-explorer}

![](./img/pio-home-inspect-firmware-file-explorer.png)

File Symbols

![](./img/pio-home-inspect-firmware-file-explorer-symbols.png)

#### Firmware Symbols {#firmware-symbols}

![](./img/pio-home-inspect-firmware-symbols.png)

#### Firmware Sections {#firmware-sections}

![](./img/pio-home-inspect-firmware-sections.png)

#### Static Code Analysis {#static-code-analysis}

![](./img/pio-home-inspect-code-defects.png)

### Library Manager {#library-manager}

![](./img/pio-home-library-stats.png)

### Board Explorer {#board-explorer}

![](./img/pio-home-boards.png)

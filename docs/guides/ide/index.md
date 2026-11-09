---
description: Use PlatformIO with Visual Studio Code, CLion, Neovim, Vim, Emacs, Eclipse and other editors and IDEs.
---

<a id="ide"></a>

# IDE integrations {#cloud-desktop-ides}

<a id="native-extensions"></a>

## Official extensions {#official-extensions}

These extensions include [PlatformIO Core](../../get-started/platformio-core.md)
and [PlatformIO Home](../../get-started/platformio-home.md), and integrate
building, uploading, debugging and testing into the IDE:

| IDE | Notes |
| --- | --- |
| [PlatformIO IDE for VS Code](./vscode.md) | Recommended: the most complete and most widely used |
| [CLion](./clion.md) | Experimental |

## Other editors and IDEs {#desktop-ides}

For these, PlatformIO generates project files with
[`pio project init --ide`](../../reference/cli/pio-project/init.md#cmdoption-pio-project-init-ide),
or the editor uses the project's
[compilation database](../compile-commands.md):

- [Code::Blocks](./codeblocks.md)
- [Eclipse](./eclipse.md)
- [Emacs](./emacs.md)
- [Neovim](./neovim.md)
- [NetBeans](./netbeans.md)
- [Qt Creator](./qtcreator.md)
- [Sublime Text](./sublimetext.md)
- [Vim](./vim.md)
- [Visual Studio](./visualstudio.md)

<a id="ide-cloud"></a>

## Cloud IDEs {#cloud-ides}

- [Codeanywhere](./codeanywhere.md)
- [Eclipse Che](./eclipseche.md)
- [AWS Cloud9](./cloud9.md) (closed to new customers since July 2024)

To program boards connected to your own computer from a cloud IDE, use
[remote development](../remote-development.md).

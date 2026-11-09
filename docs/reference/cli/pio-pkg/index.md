---
description: Install, update, list and publish PlatformIO packages - development platforms, tools and libraries.
---

# pio pkg

Manage packages: development platforms, tools (toolchains, frameworks,
uploaders) and libraries. Most commands work on the current project's
dependencies by default, or on globally installed packages with `--global`.

## Commands {#commands}

| Command | Description |
| --- | --- |
| [`pio pkg install`](./install.md) | Install the project dependencies or a package |
| [`pio pkg update`](./update.md) | Update packages to the latest compatible versions |
| [`pio pkg uninstall`](./uninstall.md) | Uninstall packages |
| [`pio pkg list`](./list.md) | List installed packages |
| [`pio pkg outdated`](./outdated.md) | List outdated project packages |
| [`pio pkg search`](./search.md) | Search the PlatformIO Registry |
| [`pio pkg show`](./show.md) | Show information about a package in the registry |
| [`pio pkg exec`](./exec.md) | Run a command from a package |
| [`pio pkg pack`](./pack.md) | Create a package archive |
| [`pio pkg publish`](./publish.md) | Publish a package to the registry |
| [`pio pkg unpublish`](./unpublish.md) | Remove a package or a version from the registry |

For the options of a command, run `pio pkg COMMAND --help`.

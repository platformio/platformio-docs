---
description: Build, upload, test and monitor devices connected to remote machines with PlatformIO Remote.
---

<a id="cmd-remote"></a>

# pio remote {#platformio-remote-cli}

Work with devices connected to other computers. See
[Remote development](../../../guides/remote-development.md).

## Usage {#usage}

```bash
pio remote [OPTIONS] COMMAND [ARGS]...
```

## Options {#options}

### `-a, --agent` {#cmdoption-pio-remote-a}

Run the command only on this [remote agent](./agent.md). Repeat the option
for several agents. By default, the command uses all agents available to you.

```bash
pio remote --agent NAME_1 --agent NAME_N COMMAND
```

## Commands {#commands}

| Command | Description |
| --- | --- |
| [`pio remote agent`](./agent.md) | Start a remote agent or list the available agents |
| [`pio remote device`](./device.md) | List remote devices or open a remote serial monitor |
| [`pio remote run`](./run.md) | Build and upload a project to a remote device |
| [`pio remote test`](./test.md) | Run unit tests on a remote device |
| [`pio remote update`](./update.md) | Update the packages of remote agents |

For the options of a command, run `pio remote COMMAND --help`.

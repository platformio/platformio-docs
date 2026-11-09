---
description: Install tab completion of pio commands for Bash, Zsh or fish.
---

<a id="cmd-system-completion-install"></a>

# pio system completion install {#pio-system-completion-install}

Install tab completion of `pio` commands and options for a shell.

## Usage {#usage}

```bash
pio system completion install [OPTIONS] SHELL
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `SHELL` | The shell: `bash`, `zsh` or `fish` |

## Options {#options}

### `--path` {#cmdoption-pio-system-completion-install-path}

The file that holds the completion code for the shell. By default, the shell's
standard location is used.

## Examples {#examples}

```bash
pio system completion install fish
```

```text
PlatformIO CLI completion has been installed for fish shell to ~/.config/fish/completions/pio.fish
Please restart a current shell session
```

Restart the shell for the change to take effect.

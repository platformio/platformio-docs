<a id="cmd-system-completion-uninstall"></a>

# pio system completion uninstall {#pio-system-completion-uninstall}

## Usage {#usage}

```bash
pio system completion uninstall [OPTIONS]
```

## Description {#description}

Uninstall shell completion files or code for:

- [fish](https://fishshell.com/)
- [zsh](http://www.zsh.org/)
- [bash](https://www.gnu.org/software/bash)

### Options {#options}

#### `--path` {#cmdoption-pio-system-completion-uninstall-path}

Custom installation path of the code to be evaluated by the shell. The standard installation path is used by default.

## Examples {#examples}

```text
> pio system completion uninstall

PlatformIO CLI completion has been uninstalled for fish shell from ~/.config/fish/completions/pio.fish
Please restart a current shell session.
```

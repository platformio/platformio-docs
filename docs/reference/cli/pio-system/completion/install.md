<a id="cmd-system-completion-install"></a>

# pio system completion install {#pio-system-completion-install}

## Usage {#usage}

```bash
pio system completion install [OPTIONS] [SHELL]
```

## Description {#description}

Install tab completion support for:

- [fish](https://fishshell.com/)
- [zsh](http://www.zsh.org/)
- [bash](https://www.gnu.org/software/bash)

### Options {#options}

#### `--path` {#cmdoption-pio-system-completion-install-path}

Custom installation path of the code to be evaluated by the shell. The standard installation path is used by default.

## Examples {#examples}

```text
> pio system completion install

PlatformIO CLI completion has been installed for fish shell to ~/.config/fish/completions/pio.fish
Please restart a current shell session
```

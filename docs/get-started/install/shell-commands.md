---
description: Make the pio command available in every terminal by adding PlatformIO Core to your PATH.
---

# Install shell commands

The [installer script](./installer-script.md) and
[PlatformIO IDE](../platformio-ide.md) install PlatformIO Core into a private
virtual environment and do not add it to your `PATH`. Follow this page to run
these commands from any terminal:

| Command | What it is |
| --- | --- |
| `pio` | The PlatformIO Core CLI ([reference](../../reference/cli/index.md)) |
| `platformio` | The same tool under its full name |
| `piodebuggdb` | Shortcut for [`pio debug --interface gdb`](../../reference/cli/pio-debug.md), for IDEs that expect a GDB executable |

The commands below assume the default
[`core_dir`](../../reference/platformio-ini/platformio/core-dir.md),
`~/.platformio` (`%USERPROFILE%\.platformio` on Windows). If you changed it,
adjust the paths.

## macOS and Linux {#unix-and-unix-like}

### For your user only (recommended) {#method-1}

1. Make sure `~/.local/bin` is in your `PATH`. If it is not, add this line to
   your shell profile: `~/.profile` (Bash), `~/.zprofile` (Zsh), or both:

   ```bash
   export PATH=$PATH:$HOME/.local/bin
   ```

   :::tip

   To keep one profile for Bash and Zsh, put the line in `~/.profile` and add
   `emulate sh -c '. ~/.profile'` to `~/.zprofile`.

   :::

2. Create the links:

   ```bash
   mkdir -p ~/.local/bin
   ln -s ~/.platformio/penv/bin/platformio ~/.local/bin/platformio
   ln -s ~/.platformio/penv/bin/pio ~/.local/bin/pio
   ln -s ~/.platformio/penv/bin/piodebuggdb ~/.local/bin/piodebuggdb
   ```

3. Sign out and sign back in, so that the new `PATH` takes effect.

### For all users {#method-2}

Create the links in `/usr/local/bin` instead. The links point into your home
directory, so they do not work for other users on the same computer. This
usually requires `sudo`:

```bash
sudo mkdir -p /usr/local/bin
sudo ln -s ~/.platformio/penv/bin/platformio /usr/local/bin/platformio
sudo ln -s ~/.platformio/penv/bin/pio /usr/local/bin/pio
sudo ln -s ~/.platformio/penv/bin/piodebuggdb /usr/local/bin/piodebuggdb
```

The commands work immediately; you do not need to sign in again.

## Windows {#windows}

Add the PlatformIO scripts folder to the beginning of your user `Path`
environment variable:

```text
%USERPROFILE%\.platformio\penv\Scripts\
```

1. Open **Start**, search for **environment variables**, and select
   **Edit environment variables for your account**.
2. Select **Path**, then **Edit**.
3. Select **New**, paste the folder above, and move it to the top with
   **Move Up**.
4. Select **OK**, then open a new terminal.

## Verify {#verify}

Open a new terminal and run:

```bash
pio --version
```

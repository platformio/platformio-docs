<a id="piocore-install-shell-commands"></a>

# Install Shell Commands {#install-shell-commands}

[PlatformIO Core (CLI)](../platformio-core.md) consists of 2 standalone tools in a system:

- `platformio` or `pio` (short alias) - [CLI Guide](../../reference/cli/index.md)
- `piodebuggdb` - alias of [pio debug](../../reference/cli/pio-debug.md)

If you have [PlatformIO IDE](../platformio-ide.md) already installed, you do not need to install [PlatformIO Core (CLI)](../platformio-core.md) separately. Just link these tools with your shell:

## Unix and Unix-like {#unix-and-unix-like}

### Method 1 {#method-1}

In Unix and Unix-like systems, you can create symbolic links (symlinks) in your `$HOME/.local/bin/` directory to the necessary PlatformIO executables. This will allow you to execute `platformio` commands from any terminal emulator as long as you're logged in as the user PlatformIO is installed and configured for.

First, if it's not already the case, you should export your `$HOME/.local/bin/` directory to the PATH environmental variable. If you use Bash as your default shell, you can do it by editing either `~/.profile` or `~/.bash_profile` and adding the following line:

```bash
export PATH=$PATH:$HOME/.local/bin
```

If you use Zsh, you can either edit `~/.zprofile` and add the code above, or for supporting both, Bash and Zsh, you can first edit `~/.profile` and add the code above, then edit `~/.zprofile` and add the following line:

```bash
emulate sh -c '. ~/.profile'
```

If you don't know the difference between the two, check out [this page](https://serverfault.com/questions/261802/what-are-the-functional-differences-between-profile-bash-profile-and-bashrc).

Now that is done, or if `$HOME/.local/bin/` was already exported to your PATH environmental variable, you can create the symlinks by opening your system terminal app and paste these commands.

```bash
ln -s ~/.platformio/penv/bin/platformio ~/.local/bin/platformio
ln -s ~/.platformio/penv/bin/pio ~/.local/bin/pio
ln -s ~/.platformio/penv/bin/piodebuggdb ~/.local/bin/piodebuggdb
```

After everything's done, just restart your session (log out and log back in) and you're good to go.

### Method 2 {#method-2}

You can create system-wide symlinks. This method is not recommended if you have multiple users on your computer because the symlinks will be broken for other users and they will get errors while executing PlatformIO commands. If that's not a problem, open your system terminal app and paste these commands. (**PROBABLY requires** administrator access `sudo`):

```bash
mkdir -p /usr/local/bin
ln -s ~/.platformio/penv/bin/platformio /usr/local/bin/platformio
ln -s ~/.platformio/penv/bin/pio /usr/local/bin/pio
ln -s ~/.platformio/penv/bin/piodebuggdb /usr/local/bin/piodebuggdb
```

After that, you should be able to run PlatformIO from terminal. No restart is required.

## Windows {#windows}

Please read one of these instructions [How do I set or change the PATH system variable?](https://www.google.com.ua/search?q=how+do+i+set+or+change+the+path+system+variable)

You need to edit the system environment variable called `Path` and append `%USERPROFILE%\.platformio\penv\Scripts\` path in the beginning of the list.

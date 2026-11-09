---
description: Create a PlatformIO Account from the command line.
---

<a id="cmd-account-register"></a>

# pio account register {#pio-account-register}

Create a [PlatformIO Account](../../../get-started/platformio-account.md). The command asks for every option you omit.

## Usage {#usage}

```bash
pio account register [OPTIONS]
```

## Options {#options}

<a id="cmdoption-pio-account-register-u"></a>

### `-u, --username` {#cmdoption-pio-account-register-username}

The username. You use it with [`pio account login`](./login.md), [`pio account update`](./update.md) and [`pio account forgot`](./forgot.md).

Usernames can contain letters, digits and single hyphens, cannot begin or end
with a hyphen, and can be up to 38 characters long.

<a id="cmdoption-pio-account-register-e"></a>

### `-e, --email` {#cmdoption-pio-account-register-email}

Your email address. PlatformIO sends a confirmation email to it.

<a id="cmdoption-pio-account-register-p"></a>

### `-p, --password` {#cmdoption-pio-account-register-password}

The password. When asked for it interactively, you enter it twice.

### `--firstname` {#cmdoption-pio-account-register-firstname}

Your first name.

### `--lastname` {#cmdoption-pio-account-register-lastname}

Your last name.

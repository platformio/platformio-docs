<a id="cmd-account-register"></a>

# pio account register {#pio-account-register}

## Usage {#usage}

```bash
pio account register [OPTIONS]
```

## Description {#description}

Create a new [PlatformIO Account](../../../get-started/platformio-account.md).

### Options {#options}

You can omit these options and enter them later in Register Wizard.

<a id="cmdoption-pio-account-register-u"></a>

#### `--username, -u` {#cmdoption-pio-account-register-username}

A username. You can use it later for [pio account login](./login.md), [pio account update](./update.md), and [pio account forgot](./forgot.md) commands.

The username must contain at least 4 characters including single hyphens, and cannot begin or end with a hyphen.

<a id="cmdoption-pio-account-register-e"></a>

#### `--email, -e` {#cmdoption-pio-account-register-email}

An email. Please enter existing email, you will receive a confirmation letter.

<a id="cmdoption-pio-account-register-p"></a>

#### `--password, -p` {#cmdoption-pio-account-register-password}

A password. You will need it for [pio account login](./login.md), [pio account password](./password.md), [pio account token](./token.md), and [pio account update](./update.md) commands.

#### `--firstname` {#cmdoption-pio-account-register-firstname}

A first name.

#### `--lastname` {#cmdoption-pio-account-register-lastname}

A last name.

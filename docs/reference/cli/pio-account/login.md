<a id="cmd-account-login"></a>

# pio account login {#pio-account-login}

## Usage {#usage}

```bash
pio account login [OPTIONS]
```

## Description {#description}

Log in to [PlatformIO Account](../../../get-started/platformio-account.md). If you are not able to provide authentication credentials manually you can use [`PLATFORMIO_AUTH_TOKEN`](../../environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN). This is very useful for [Continuous Integration](../../../guides/ci/index.md) systems and [Remote Development](../../../guides/remote-development.md) operations.

### Options {#options}

<a id="cmdoption-pio-account-login-u"></a>

#### `--username, -u` {#cmdoption-pio-account-login-username}

Username or email. You can omit this option and enter username or email in Login Wizard later.

<a id="cmdoption-pio-account-login-p"></a>

#### `--password, -p` {#cmdoption-pio-account-login-password}

You can omit this option and enter securely password in Login Wizard later.

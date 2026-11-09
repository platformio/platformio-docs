---
description: Sign in to your PlatformIO Account.
---

<a id="cmd-account-login"></a>

# pio account login {#pio-account-login}

Sign in to your [PlatformIO Account](../../../get-started/platformio-account.md).

## Usage {#usage}

```bash
pio account login [OPTIONS]
```

## Description {#description}

Where you cannot sign in interactively, for example in
[CI](../../../guides/ci/index.md) or for
[remote development](../../../guides/remote-development.md) agents, set the
[`PLATFORMIO_AUTH_TOKEN`](../../environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN)
environment variable instead. Get a token with [`pio account token`](./token.md).

## Options {#options}

<a id="cmdoption-pio-account-login-u"></a>

### `-u, --username` {#cmdoption-pio-account-login-username}

Your username or email. If you omit it, the command asks for it.

<a id="cmdoption-pio-account-login-p"></a>

### `-p, --password` {#cmdoption-pio-account-login-password}

Your password. If you omit it, the command asks for it without showing what you type.

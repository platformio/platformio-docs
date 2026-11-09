---
description: Get or regenerate the personal authentication token of your PlatformIO Account.
---

# pio account token

Get or regenerate the personal authentication token of your [PlatformIO Account](../../../get-started/platformio-account.md).

## Usage {#usage}

```bash
pio account token [OPTIONS]
```

## Description {#description}

Use the token where you cannot sign in interactively, such as in
[CI](../../../guides/ci/index.md) or for
[remote development](../../../guides/remote-development.md): set it in the
[`PLATFORMIO_AUTH_TOKEN`](../../environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN)
environment variable.

:::warning

The token gives full access to your account. Keep it secret, for example in
your CI service's secret store.

:::

## Options {#options}

### `-p, --password` {#cmdoption-pio-account-token-password}

Your password. If you omit it, the command asks for it.

### `--regenerate` {#cmdoption-pio-account-token-regenerate}

Generate a new token. The previous token stops working.

### `--json-output` {#cmdoption-pio-account-token-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

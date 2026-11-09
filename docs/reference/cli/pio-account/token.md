<a id="cmd-account-token"></a>

# pio account token {#pio-account-token}

## Usage {#usage}

```bash
pio account token
```

## Description {#description}

Get or regenerate Personal Authentication Token. It is very useful for [Continuous Integration](../../../guides/ci/index.md) systems, [Remote Development](../../../guides/remote-development.md) operations where you are not able to authorize manually.

PlatformIO handles Personal Authentication Token from environment variable [`PLATFORMIO_AUTH_TOKEN`](../../environment-variables.md#envvar-PLATFORMIO_AUTH_TOKEN).

### Options {#options}

#### `--regenerate` {#cmdoption-pio-account-token-regenerate}

If this option is specified a new authentication token will be generated.

#### `--json-output` {#cmdoption-pio-account-token-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format

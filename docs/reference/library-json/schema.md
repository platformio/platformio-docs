---
description: "A JSON Schema to annotate and validate the library.json manifest."
---

<a id="manifest-library-json-schema"></a>

# `$schema` {#schema}

- **Required:** No
- **Type:** String

A [JSON Schema](https://json-schema.org/) to annotate and validate the `library.json` manifest. The [PlatformIO IDE for VSCode](../../guides/ide/vscode.md) has built-in support for JSON Schema validation.

You can also validate the `library.json` manifest file using the [pio pkg pack](../cli/pio-pkg/pack.md) command.

The `library.json` Schema URL:

```bash
https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/schema/library.json
```

## Example

```javascript
{
  "$schema": "https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/schema/library.json",
  "name": "Foo",
  "version": "1.0.0"
}
```

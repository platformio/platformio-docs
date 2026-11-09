---
description: Create an organization in PlatformIO.
---

<a id="cmd-org-create"></a>

# pio org create {#pio-org-create}

Create an organization. You become its owner.

## Usage {#usage}

```bash
pio org create [OPTIONS] ORGNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | The organization name. Organization names can contain letters, digits and single hyphens, cannot begin or end with a hyphen, and can be up to 38 characters long. |

## Options {#options}

### `--email` {#cmdoption-pio-org-create-email}

The organization's email address.

### `--displayname` {#cmdoption-pio-org-create-displayname}

The display name, for example the company name.

## Examples {#examples}

```bash
pio org create platformio --email contact@platformio.org --displayname PlatformIO
```

```text
The organization "platformio" has been successfully created.
```

## See also {#see-also}

- [`pio org update`](./update.md)
- [`pio org destroy`](./destroy.md)

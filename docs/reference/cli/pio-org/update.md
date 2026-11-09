---
description: Rename an organization or update its details.
---

# pio org update

Rename an organization or update its details.

## Usage {#usage}

```bash
pio org update [OPTIONS] ORGNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | The current organization name |

## Options {#options}

### `--orgname` {#cmdoption-pio-org-update-orgname}

A new organization name. Organization names can contain letters, digits and single hyphens, cannot
begin or end with a hyphen, and can be up to 38 characters long.

### `--email` {#cmdoption-pio-org-update-email}

A new email address.

### `--displayname` {#cmdoption-pio-org-update-displayname}

A new display name, for example the company name.

## Examples {#examples}

```bash
pio org update platformio --email contact@platformio.org --displayname PlatformIO
```

```text
The organization "platformio" has been successfully updated.
```

## See also {#see-also}

- [`pio org create`](./create.md)

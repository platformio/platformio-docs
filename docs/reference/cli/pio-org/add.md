---
description: Add an owner to an organization.
---

<a id="cmd-org-add"></a>

# pio org add {#pio-org-add}

Add a user as an owner of an organization.

## Usage {#usage}

```bash
pio org add ORGNAME USERNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | The organization |
| `USERNAME` | The user to add as an owner |

## Examples {#examples}

Add `bob` as an owner of the `platformio` organization:

```bash
pio org add platformio bob
```

```text
The new owner "bob" has been successfully added to the "platformio" organization.
```

## See also {#see-also}

- [`pio org create`](./create.md)
- [`pio org remove`](./remove.md)

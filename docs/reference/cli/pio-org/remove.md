---
description: Remove an owner from an organization.
---

# pio org remove

Remove an owner from an organization.

## Usage {#usage}

```bash
pio org remove ORGNAME USERNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | The organization |
| `USERNAME` | The owner to remove |

To delete the whole organization, use [`pio org destroy`](./destroy.md).

## Examples {#examples}

Remove `bob` from the `platformio` organization:

```bash
pio org remove platformio bob
```

```text
The `bob` owner has been successfully removed from the `platformio` organization.
```

## See also {#see-also}

- [`pio org add`](./add.md)
- [`pio org destroy`](./destroy.md)

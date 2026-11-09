---
description: Delete an organization and its teams.
---

# pio org destroy

Delete an organization and all its teams.

## Usage {#usage}

```bash
pio org destroy ORGNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | The organization to delete |

:::danger

This cannot be undone. The command asks for confirmation before it deletes
anything.

:::

To remove a single owner instead, use [`pio org remove`](./remove.md).

## See also {#see-also}

- [`pio org create`](./create.md)
- [`pio org remove`](./remove.md)

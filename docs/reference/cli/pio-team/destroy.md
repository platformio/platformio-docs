---
description: Delete a team.
---

# pio team destroy

Delete a team.

## Usage {#usage}

```bash
pio team destroy ORGNAME:TEAMNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` | The team to delete, prefixed with its organization |

:::danger

This cannot be undone. The command asks for confirmation before it deletes
anything.

:::

To remove a single member instead, use [`pio team remove`](./remove.md).

## See also {#see-also}

- [`pio team create`](./create.md)
- [`pio team remove`](./remove.md)

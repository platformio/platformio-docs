---
description: Remove a member from a team.
---

<a id="cmd-team-remove"></a>

# pio team remove {#pio-team-remove}

Remove a member from a team.

## Usage {#usage}

```bash
pio team remove ORGNAME:TEAMNAME USERNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` | The team, prefixed with its organization |
| `USERNAME` | The member to remove |

To delete the whole team, use [`pio team destroy`](./destroy.md).

## Examples {#examples}

Remove `bob` from the `dev` team of the `platformio` organization:

```bash
pio team remove platformio:dev bob
```

```text
The "bob" member has been successfully removed from the "dev" team.
```

## See also {#see-also}

- [`pio team add`](./add.md)
- [`pio team destroy`](./destroy.md)

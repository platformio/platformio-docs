---
description: Add a member to a team.
---

<a id="cmd-team-add"></a>

# pio team add {#pio-team-add}

Add a user to a team.

## Usage {#usage}

```bash
pio team add ORGNAME:TEAMNAME USERNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` | The team, prefixed with its organization |
| `USERNAME` | The user to add |

## Examples {#examples}

Add `bob` to the `developers` team of the `platformio` organization:

```bash
pio team add platformio:developers bob
```

```text
The new member "bob" has been successfully added to the "developers" team.
```

## See also {#see-also}

- [`pio team create`](./create.md)
- [`pio team remove`](./remove.md)

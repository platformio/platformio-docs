---
description: Create a team in an organization.
---

# pio team create

Create a team in an organization.

## Usage {#usage}

```bash
pio team create [OPTIONS] ORGNAME:TEAMNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` | The organization and the new team's name. Team names can contain letters, digits, and single hyphens, underscores or spaces between them, and can be up to 20 characters long. |

## Options {#options}

### `--description` {#cmdoption-pio-team-create-description}

A description of the team.

## Examples {#examples}

```bash
pio team create platformio:dev --description "Developers team"
```

```text
The team "dev" has been successfully created.
```

## See also {#see-also}

- [`pio team update`](./update.md)
- [`pio team destroy`](./destroy.md)

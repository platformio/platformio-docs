---
description: Rename a team or update its description.
---

<a id="cmd-team-update"></a>

# pio team update {#pio-team-update}

Rename a team or update its description.

## Usage {#usage}

```bash
pio team update [OPTIONS] ORGNAME:TEAMNAME
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME:TEAMNAME` | The team, prefixed with its organization |

## Options {#options}

### `--name` {#cmdoption-pio-team-update-name}

A new team name. Team names can contain letters, digits, and single hyphens, underscores or
spaces between them, and can be up to 20 characters long.

### `--description` {#cmdoption-pio-team-update-description}

A new description.

## Examples {#examples}

```bash
pio team update platformio:dev --description "Developers team"
```

```text
The team "dev" has been successfully updated.
```

## See also {#see-also}

- [`pio team create`](./create.md)

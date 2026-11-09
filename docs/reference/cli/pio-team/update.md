<a id="cmd-team-update"></a>

# pio team update {#pio-team-update}

## Usage {#usage}

```bash
pio team update [OPTIONS] ORGNAME:TEAMNAME
```

## Description {#description}

Rename a team or update the existing details.

### Options {#options}

#### `--name` {#cmdoption-pio-team-update-name}

A new team name. Team name must only contain alphanumeric characters, single hyphens, underscores, spaces. It can not begin or end with a hyphen or a underscore and must not be longer than 20 characters.

#### `--description` {#cmdoption-pio-team-update-description}

A team description.

## Examples {#examples}

```bash
> pio team update platformio:dev --description "Developers team"
The team "dev" has been successfully updated.
```

## See Also {#see-also}

- [pio team list](./list.md)
- [pio team remove](./remove.md)

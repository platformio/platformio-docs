<a id="cmd-team-add"></a>

# pio team add {#pio-team-add}

## Usage {#usage}

```bash
pio team add ORGNAME:TEAMNAME USERNAME
```

## Description {#description}

Add a new member to a team.

If you need to create a new team, please use [pio team create](./create.md) command.

## Examples {#examples}

Add Bob to the "developers" team of "platformio" organization

```bash
> pio team add platformio:developers bob
The new member "bob" has been successfully added to the "developers" team.
```

## See Also {#see-also}

- [pio team create](./create.md)
- [pio team list](./list.md)
- [pio team remove](./remove.md)

<a id="cmd-team-remove"></a>

# pio team remove {#pio-team-remove}

## Usage {#usage}

```bash
pio team remove ORGNAME:TEAMNAME USERNAME
```

## Description {#description}

Remove a member from a team.

If you need to destroy an existing team, please use [pio team destroy](./destroy.md) command.

## Examples {#examples}

Remove Bob from the "dev" team of "platformio" organization:

```bash
> pio team remove platformio:dev bob
The "bob" member has been successfully removed from the "dev" team.
```

## See Also {#see-also}

- [pio team add](./add.md)
- [pio team list](./list.md)

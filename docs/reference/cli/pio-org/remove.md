<a id="cmd-org-remove"></a>

# pio org remove {#pio-org-remove}

## Usage {#usage}

```bash
pio org remove ORGNAME USERNAME
```

## Description {#description}

Remove a user from an organization.

If you need to destroy an existing organization, please use [pio org destroy](./destroy.md) command.

## Examples {#examples}

Remove Bob from "platformio" organization:

```bash
> pio org remove platformio bob
The `bob` owner has been successfully removed from the `platformio` organization.
```

## See Also {#see-also}

- [pio org add](./add.md)
- [pio org list](./list.md)

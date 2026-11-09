<a id="cmd-org-add"></a>

# pio org add {#pio-org-add}

## Usage {#usage}

```bash
pio org add ORGNAME USERNAME
```

## Description {#description}

Add a user as an owner to an organization.

If you need to create a new organization, please use [pio org create](./create.md) command.

## Examples {#examples}

Add Bob as an owner of "platformio" organization:

```bash
> pio org add platformio bob
The new owner "bob" has been successfully added to the "platformio" organization.
```

## See Also {#see-also}

- [pio org create](./create.md)
- [pio org list](./list.md)
- [pio org remove](./remove.md)

<a id="cmd-org-update"></a>

# pio org update {#pio-org-update}

## Usage {#usage}

```bash
pio org update [OPTIONS] ORGNAME
```

## Description {#description}

Rename the organization or update the existing details.

### Options {#options}

#### `--orgname` {#cmdoption-pio-org-update-orgname}

New organization "orgname". Must contain only alphanumeric characters or single hyphens, cannot begin or end with a hyphen, and must not be longer than 38 characters.

#### `--email` {#cmdoption-pio-org-update-email}

An organization e-mail.

#### `--displayname` {#cmdoption-pio-org-update-displayname}

An organization name (company name).

## Examples {#examples}

```bash
> pio org update platformio --email contact@platformio.org --displayname PlatformIO
The organization "platformio" has been successfully updated.
```

## See Also {#see-also}

- [pio org list](./list.md)
- [pio org remove](./remove.md)

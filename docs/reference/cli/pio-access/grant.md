<a id="cmd-access-grant"></a>

# pio access grant {#pio-access-grant}

## Usage {#usage}

```bash
pio access grant [OPTIONS] LEVEL <ORGNAME:TEAMNAME>|<USERNAME> URN
```

## Description {#description}

Add the ability of users and teams to have "LEVEL" access to a resource.

The next levels are supported:

<dl>

<dt>

`admin`

</dt>

<dd>

Administrative privileges. Can perform all available operations on the particular resource.

</dd>

<dt>

`maintainer`

</dt>

<dd>

Read-write access. Can update a resource, publish a new version, unpublish existing version.

Cannot manage resource permissions and grant access to other members.

</dd>

<dt>

`guest`

</dt>

<dd>

Read-only access. It's automatically granted for the public resources.

</dd>

</dl>

You can grant access to the team members using the next format `orgname:teamname`. See the examples below.

### Options {#options}

#### `--urn-type` {#cmdoption-pio-access-grant-urn-type}

Resource type in [URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name) form. Default is set to `prn:reg:pkg` which means to grant an access to the package in the PlatormIO Registry.

## Examples {#examples}

1. Grant "maintainer" access to a resource for the "bob" user:

```bash
> pio access grant maintainer bob prn:reg:pkg:8036:platform
Access for resource "prn:reg:pkg:8036:platform" has been granted for "bob"
```

2. Add the ability of PlatformIO's "developer" team to have "admin" access to a resource.

```bash
> pio access grant admin platformio:developers prn:reg:pkg:8036:platform
Access for resource "prn:reg:pkg:8036:platform" has been granted for "platformio:developers"
```

## See Also {#see-also}

- [pio access revoke](./revoke.md)

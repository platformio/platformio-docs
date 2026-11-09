<a id="cmd-access-list"></a>

# pio access list {#pio-access-list}

## Usage {#usage}

```bash
pio access list [OPTIONS] [OWNER]
```

## Description {#description}

Show all of the resources (packages) a user or a team can access, along with the access level, except for read-only public resources (it won’t print the whole registry listing).

To list resources by the specified owner, type owner's "username" as an argument to this command.

See the examples below.

### Options {#options}

#### `--urn-type` {#cmdoption-pio-access-list-urn-type}

Resource type in [URN](https://en.wikipedia.org/wiki/Uniform_Resource_Name) form. Default is set to `prn:reg:pkg` which means to list the packages from the registry.

#### `--json-output` {#cmdoption-pio-access-list-json-output}

Return the output in [JSON](http://en.wikipedia.org/wiki/JSON) format

## Examples {#examples}

1. List all accessible resources:

```bash
> pio access list

...

atmelsam
--------
URN:              prn:reg:pkg:8007:platform
Owner:            platformio
Access level(s):  Admin

espressif8266
-------------
URN:              prn:reg:pkg:8008:platform
Owner:            platformio
Access level(s):  Admin

chipsalliance
-------------
URN:              prn:reg:pkg:8036:platform
Owner:            platformio
Access level(s):  Admin

contrib-piohome
---------------
URN:              prn:reg:pkg:8037:tool
Owner:            platformio
Access level(s):  Admin

...
```

2. List all accessible resources by specific owner:

```bash
> pio access list platformio

...

tool-scons
----------
URN:              prn:reg:pkg:8192:tool
Owner:            platformio
Access level(s):  Admin

tool-simavr
-----------
URN:              prn:reg:pkg:8193:tool
Owner:            platformio
Access level(s):  Admin

...
```

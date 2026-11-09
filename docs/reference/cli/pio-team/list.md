---
description: List teams and their members.
---

# pio team list

List the teams and their members.

## Usage {#usage}

```bash
pio team list [OPTIONS] [ORGNAME]
```

## Description {#description}

| Argument | Description |
| --- | --- |
| `ORGNAME` | Optional. List only the teams of this organization. |

## Options {#options}

### `--json-output` {#cmdoption-pio-team-list-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

## Examples {#examples}

```bash
pio team list
```

```text
platformio:dev
------------------------
Description:  Developers team
Members:      alice, bob
```

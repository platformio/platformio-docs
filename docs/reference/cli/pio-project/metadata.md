---
description: Show the build metadata of a project - toolchain, flags, defines and include paths - for IDE integrations.
---

<a id="cmd-project-metadata"></a>

# pio project metadata {#pio-project-metadata}

Show the build metadata of a project. IDE extensions and code analysis tools
use it to configure code completion and navigation.

## Usage {#usage}

```bash
pio project metadata [OPTIONS]
```

## Description {#description}

For each environment, the metadata includes:

- the toolchain type and location;
- the compiler flags, defines and include paths;
- the path of the built program;
- the SVD file of the MCU, if the development platform provides one;
- the [project targets](../pio-run.md#cmdoption-pio-run-list-targets) and other
  platform-specific information.

## Options {#options}

<a id="cmdoption-pio-project-metadata-project-dir"></a>

### `-d, --project-dir` {#cmdoption-pio-project-metadata-d}

The project directory. Default: the current working directory.

<a id="cmdoption-pio-project-metadata-environment"></a>

### `-e, --environment` {#cmdoption-pio-project-metadata-e}

Show the metadata of this environment only. Repeat the option for several
environments.

### `--json-output` {#cmdoption-pio-project-metadata-json-output}

Print the result in [JSON](https://en.wikipedia.org/wiki/JSON) format.

### `--json-output-path` {#cmdoption-pio-project-metadata-json-output-path}

Save the metadata in JSON format to this file. If you pass a folder, the file
name is generated. The folder must exist.

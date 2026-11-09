---
description: Build options of the platformio.ini [env] section.
---

<a id="projectconf-section-env-build"></a>

# Build options {#build-options}

Control how the project is compiled and linked.

| Option | Description |
| --- | --- |
| [`build_type`](./build-type.md) | Project build configuration |
| [`build_flags`](./build-flags.md) | Custom build flags/options for preprocessing, compilation, assembly, and linking processes |
| [`build_src_flags`](./build-src-flags.md) | The same as `build_flags` but configures flags the only for project source files in the `src` folder |
| [`build_unflags`](./build-unflags.md) | A list with flags/option which should be removed |
| [`build_src_filter`](./build-src-filter.md) | Control which source files from the `src` folder should be included/excluded from a build process |
| [`targets`](./targets.md) | A custom list of targets for PlatformIO Build System |

---
description: Directory options of the platformio.ini [platformio] section.
---

# Directory options

Locations of PlatformIO data and of the project folders. Paths can be absolute or relative to the project directory.

| Option | Description |
| --- | --- |
| [`core_dir`](./core-dir.md) | PlatformIO Core location where it keeps installed development platforms, packages, global libraries, and other internal information |
| [`globallib_dir`](./globallib-dir.md) | A library folder/storage where PlatformIO Library Dependency Finder (LDF) looks for global libraries |
| [`platforms_dir`](./platforms-dir.md) | A location where PlatformIO Core keeps installed development platforms |
| [`packages_dir`](./packages-dir.md) | A location where PlatformIO Core keeps installed packages |
| [`cache_dir`](./cache-dir.md) | A location where PlatformIO Core stores caching information (requests to PlatformIO Registry, downloaded packages and other service information) |
| [`build_cache_dir`](./build-cache-dir.md) | A location where PlatformIO Core keeps derived files from a build system (objects, firmwares, ELFs) and caches them between build environments |
| [`workspace_dir`](./workspace-dir.md) | A path to a project workspace directory where PlatformIO keeps by default compiled objects, static libraries, firmwares, and external library dependencies |
| [`build_dir`](./build-dir.md) | PlatformIO Build System uses this folder for project environments to store compiled object files, static libraries, firmwares, and other cached information |
| [`libdeps_dir`](./libdeps-dir.md) | Internal storage where Library Manager will install project dependencies declared via `lib_deps` option |
| [`include_dir`](./include-dir.md) | A default location for project header files. PlatformIO Build System automatically adds this path to CPPPATH scope |
| [`src_dir`](./src-dir.md) | A default location where PlatformIO Build System looks for the project C/C++ source files |
| [`lib_dir`](./lib-dir.md) | A storage for the custom/private project libraries |
| [`data_dir`](./data-dir.md) | A data directory to store contents which can be uploaded to file system (SPIFFS, etc.) |
| [`test_dir`](./test-dir.md) | A location where PlatformIO Unit Testing engine looks for test source files |
| [`boards_dir`](./boards-dir.md) | A storage for custom board manifests |
| [`monitor_dir`](./monitor-dir.md) | A storage for custom monitor filters |
| [`shared_dir`](./shared-dir.md) | A location which PlatformIO Remote Development service uses to synchronize extra files between remote machines |

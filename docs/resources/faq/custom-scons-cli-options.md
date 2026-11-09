---
description: Pass SCons command-line options, such as --dry-run or --debug=explain, to the PlatformIO build.
---

# Pass options to SCons {#custom-scons-command-line-options}

The PlatformIO build system runs on [SCons](https://scons.org/). SCons options
can help you understand what happens during a build, for example:

| Option | What it does |
| --- | --- |
| `--dry-run` | Print the commands that would run, without running them |
| `--tree=all` | Print the dependency tree of the files, including implicit dependencies |
| `--debug=explain` | Explain why each target is rebuilt |

See the [SCons documentation](https://scons.org/doc/production/HTML/scons-user/ch10.html#sect-command-line-options)
for all options.

To pass options to SCons, set the `SCONSFLAGS` environment variable before
running `pio run`:

```text
# POSIX shell
export SCONSFLAGS="--tree=all"

# Windows CMD
C:\Users\foo> set SCONSFLAGS=--dry-run
```

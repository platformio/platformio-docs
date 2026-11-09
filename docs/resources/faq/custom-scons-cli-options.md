# Custom SCons command-line options {#custom-scons-command-line-options}

PlatformIO is built on top of the open-source software construction tool called SCons. SCons has many useful command-line options that control its behavior and may come in handy to know the exact internal processes happening in SCons when it builds a target. For example:

- `--dry-run` configures SCons to print the commands that would be executed to build any target, but do not execute the commands.
- `--tree=all` forces SCons to print file dependency tree including implicit and ignored dependencies
- `--debug=explain` will print an explanation of why SCons decides to (re-)build the targets it selects for building.

The list of available command-line options can be found in the official [SCons documentation](https://scons.org/doc/production/HTML/scons-user/ch10.html#sect-command-line-options).

The easiest way to pass extra command-line options to the SCons build system used in PlatformIO is via the external `SCONSFLAGS` environment variable:

```text
# POSIX shell
export SCONSFLAGS="--tree=all"

# Windows CMD
C:\Users\foo> set SCONSFLAGS=--dry-run
```

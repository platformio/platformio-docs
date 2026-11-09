<a id="projectconf-debug-load-mode"></a>

# `debug_load_mode` {#debug-load-mode}

Type: `String` | Multiple: `No` | Default: `always`

Allows one to control when PlatformIO should load debugging firmware to the end target. Possible options:

- `always` - load for the each debugging session, **default**
- `modified` - load only when firmware was modified
- `manual` - do not load firmware automatically. You are responsible to pre-flash target with debugging firmware in this case.

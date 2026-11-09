---
description: Start the PlatformIO Home server from the command line.
---

# pio home

Start the [PlatformIO Home](../../get-started/platformio-home.md) web server
and open it in your browser.

## Usage {#usage}

```bash
pio home [OPTIONS]
```

## Options {#options}

### `--port` {#cmdoption-pio-home-port}

The HTTP port. Default: `8008`.

### `--host` {#cmdoption-pio-home-host}

The HTTP host. Default: `127.0.0.1`, which accepts connections only from this
computer. Use `0.0.0.0` to accept connections from other computers.

### `--no-open` {#cmdoption-pio-home-no-open}

Do not open PlatformIO Home in the browser.

### `--shutdown-timeout` {#cmdoption-pio-home-shutdown-timeout}

Stop the server after this many seconds without connected clients. Default:
`0`, which means never.

### `--session-id` {#cmdoption-pio-home-session-id}

A unique session ID that isolates this PlatformIO Home instance from others
and protects it from access by third parties.

:::warning

Without a session ID, any user on this computer who knows the host and port
can open your PlatformIO Home.

:::

## Examples {#examples}

```bash
pio home
```

```text
  ___I_
 /\-_--\   PlatformIO Home
/  \_-__\
|[]| [] |  http://127.0.0.1:8008
|__|____|_______________________

Open PlatformIO Home in your browser by this URL => http://127.0.0.1:8008
PlatformIO Home has been started. Press Ctrl+C to shutdown.
```

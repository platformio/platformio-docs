<a id="cmd-home"></a>

# pio home {#pio-home}

Helper command for [PlatformIO Home](../../get-started/platformio-home.md).

## Usage {#usage}

```bash
pio home
```

## Description {#description}

Launch [PlatformIO Home](../../get-started/platformio-home.md) Web-server.

## Options {#options}

### `--port` {#cmdoption-pio-home-port}

Web-server HTTP port, default is `8008`.

### `--host` {#cmdoption-pio-home-host}

Web-server HTTP host, default is `127.0.0.1`. You can open PlatformIO Home for inbound connections using host `0.0.0.0`.

### `--no-open` {#cmdoption-pio-home-no-open}

Do not automatically open PlatformIO Home in a system Web-browser.

### `--shutdown-timeout` {#cmdoption-pio-home-shutdown-timeout}

Automatically shutdown server on timeout (in seconds) when no clients are connected. Default is `0` which means never auto shutdown.

### `--session-id` {#cmdoption-pio-home-session-id}

A unique session identifier to keep PlatformIO Home isolated from other instances and protect from 3rd party access.

:::warning

If a unique session ID is not specified (default mode), PlatformIO Home will be accessible by any user from your machine using if he knows `--host` and `--port`.

:::

## Examples {#examples}

```text
> pio home

  ___I_
 /\-_--\   PlatformIO Home
/  \_-__\
|[]| [] |  http://127.0.0.1:8008
|__|____|_______________________

Open PlatformIO Home in your browser by this URL => http://127.0.0.1:8008
PlatformIO Home has been started. Press Ctrl+C to shutdown.
```

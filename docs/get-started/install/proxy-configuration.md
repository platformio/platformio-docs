---
description: Use PlatformIO Core behind an HTTP, HTTPS or SOCKS proxy.
---

<a id="piocore-install-proxy-configuration"></a>

# Configure a proxy {#proxy-configuration}

PlatformIO Core makes HTTP requests through the Python
[Requests](https://requests.readthedocs.io/) library, which reads the standard
proxy environment variables.

1. Set the variable for your proxy type before you run `pio`:

   ```bash
   # HTTP proxy with authentication
   export HTTP_PROXY="http://user:pass@10.10.1.10:3128/"

   # HTTPS proxy
   export HTTPS_PROXY="http://10.10.1.10:1080"

   # SOCKS proxy for all protocols
   export ALL_PROXY="socks5://10.10.1.10:3434"
   ```

   On Windows (Command Prompt), use `set`:

   ```bash
   set HTTP_PROXY=http://user:pass@10.10.1.10:3128/
   ```

2. If your proxy intercepts TLS with its own certificate, turn off strict
   certificate verification for proxied requests with the
   [`enable_proxy_strict_ssl`](../../reference/cli/pio-settings.md#setting-enable-proxy-strict-ssl)
   setting:

   ```bash
   pio settings set enable_proxy_strict_ssl false
   ```

   Or set it for the current session only:

   ```bash
   export PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL="false"
   ```

For other proxy and certificate options, see
[Proxies](https://requests.readthedocs.io/en/latest/user/advanced/#proxies) in
the Requests documentation.

<a id="piocore-install-proxy-configuration"></a>

# Proxy Configuration {#proxy-configuration}

PlatformIO Core uses Python's underlying `requests` library for HTTP requests. You will need to define a standard environment variable (`HTTP_PROXY`, `HTTPS_PROXY`, or `ALL_PROXY`) depending on your proxy server, and disable the proxy server certificate verification setting [enable_proxy_strict_ssl](../../reference/cli/pio-settings.md#setting-enable-proxy-strict-ssl) to `false`.

See other proxy and SSL configuration environment variables in the official [Requests Proxies](https://requests.readthedocs.io/en/latest/user/advanced/#proxies) documentation.

**Examples**

```bash
# Disable proxy server certificate verification
$ pio settings set enable_proxy_strict_ssl false

# or using global environment variable
$ export PLATFORMIO_SETTING_ENABLE_PROXY_STRICT_SSL="false"

#
# Configure proxy server
#

# Unix
$ export HTTP_PROXY="HTTP_PROXY=http://user:pass@10.10.1.10:3128/"
# without authentication
$ export HTTPS_PROXY="http://10.10.1.10:1080"
$ export ALL_PROXY="socks5://10.10.1.10:3434"

# Windows
set HTTP_PROXY=http://user:pass@10.10.1.10:3128/
```

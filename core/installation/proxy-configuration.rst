..  Copyright (c) 2014-present PlatformIO <contact@platformio.org>
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

.. _piocore_install_proxy_configuration:

Proxy Configuration
-------------------

PlatformIO Core uses Python's underlying ``requests`` library for HTTP requests.
You will need to define a standard environment variable (``HTTP_PROXY``,
``HTTPS_PROXY``, or ``ALL_PROXY``) depending on your proxy server, and
disable the proxy server certificate verification setting
:ref:`setting_enable_proxy_strict_ssl` to ``false``.

See other proxy and SSL configuration environment variables in the
official `Requests Proxies <https://requests.readthedocs.io/en/latest/user/advanced/#proxies>`__
documentation.

**Examples**

.. code:: bash

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


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

.. _projectconf_dynamic_vars:

Dynamic variables
-----------------

Dynamic variables (interpolations) are useful when you have a custom
configuration data between build environments. For examples, extra
:ref:`projectconf_build_flags` or project dependencies :ref:`projectconf_lib_deps`.

Each variable should have a next format: ``${<section>.<option>}``, where
``<section>`` is a value from ``[<section>]`` group, and ``<option>`` is a
first item from pair ``<option> = value``.

You can inject system environment variable using ``sysenv`` as a ``section``.
For example, ``${sysenv.HOME}``.

* Variable can be applied only for the option's value
* Multiple variables are allowed
* The :ref:`projectconf_section_platformio` and :ref:`projectconf_section_env`
  sections are reserved and could not be used as a custom section. Some good
  section names might be ``extra`` or ``custom``.

.. note::
    If you need to **share common configuration options** between build
    environments, please take a look at **"Global scope"** in
    :ref:`projectconf_section_env` or :ref:`projectconf_env_extends` option which
    allows extending of other sections.

Example:

.. code-block:: ini

    ; You MUST inject these options into [env:] section
    ; using ${extra.***} (see below)
    [extra]
    build_flags = -D VERSION=1.2.3 -D DEBUG=1
    lib_deps_builtin =
      SPI
      Wire
    lib_deps_external =
      bblanchon/ArduinoJson@>5.6.0

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno
    build_flags = ${extra.build_flags}
    lib_deps =
      ${extra.lib_deps_builtin}
      ${extra.lib_deps_external}

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2
    build_flags = ${extra.build_flags} -Wall
    lib_deps =
      ${extra.lib_deps_builtin}
      ${extra.lib_deps_external}
      knolleary/PubSubClient @ ~2.6
      paulstoffregen/OneWire @ ^2.3.5

    ; Keep sensitive data in environment variables
    ;
    ; Unix
    ; export WIFI_SSID='\"my\ ssid\ name\"'
    ; export WIFI_PASS='\"my\ password\"'
    ;
    ; Windows
    ; set WIFI_SSID='"my ssid name"'
    ; set WIFI_PASS='"my password"'

    [env:esp32dev]
    extends = env:nodemcuv2
    platform = espressif32
    board = esp32dev
    build_flags =
      -DWIFI_SSID=${sysenv.WIFI_SSID}
      -DWIFI_PASS=${sysenv.WIFI_PASS}


.. warning::

    Be careful with special characters in system environment variables on Unix systems,
    especially when they are used as the value for preprocessor directives.
    Symbols like ``$``, ``&``, ``~``, etc must be explicitly escaped, for example:

    .. code-block:: bash

      export WIFI_PASS='\"my\~p\&a\\\$\$\$\$word\"'

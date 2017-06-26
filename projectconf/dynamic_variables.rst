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

.. versionadded:: 3.1

Dynamic variables/templates are useful when you have common configuration data
between build environments. For examples, common :ref:`projectconf_build_flags`
or project dependencies :ref:`projectconf_lib_deps`.

Each variable should have a next format: ``${<section>.<option>}``, where
``<section>`` is a value from ``[<section>]`` group, and ``<option>`` is a
first item from pair ``<option> = value``.

You can inject environment variable using ``env`` as a ``section``. For example,
``${env.HOME}``, etc.

* Variable can be applied only for the option's value
* Multiple variables are allowed
* The ``platformio`` and ``env`` sections are reserved and could not be used
  as custom section. Some good section names might be ``common`` or ``global``.

Example:

.. code-block:: ini

    [platformio]
    ; Unix
    lib_extra_dirs = ${env.HOME}/Documents/Arduino/libraries
    ; Windows
    lib_extra_dirs = ${env.HOMEDRIVE}${env.HOMEPATH}\Documents\Arduino\libraries


    [common]
    build_flags = -D VERSION=1.2.3 -D DEBUG=1
    lib_deps_builtin =
      SPI
      Wire
    lib_deps_external = ArduinoJson@>5.6.0

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno
    build_flags = ${common.build_flags}
    lib_deps = ${common.lib_deps_builtin}, ${common.lib_deps_external}

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2
    build_flags = ${common.build_flags} -DSSID_NAME=HELLO -DSSID_PASWORD=WORLD
    lib_deps =
      ${common.lib_deps_builtin}
      ${common.lib_deps_external}
      PubSubClient@2.6
      OneWire
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

.. _projectconf_pio_default_envs:

``default_envs``
^^^^^^^^^^^^^^^^

Type: ``String`` | Multiple: ``Yes``

The :ref:`cmd_run` command processes all environments ``[env:***]`` by default
if the :option:`pio run --environment` option is not specified.
:ref:`projectconf_pio_default_envs` allows one to define which environments that
should be processed by default.

Also, :ref:`piodebug` checks this option when looking for debug environment.

This option can also be configured by the global environment variable
:envvar:`PLATFORMIO_DEFAULT_ENVS`.

Example:

.. code-block:: ini

    [platformio]
    default_envs = uno, nodemcu

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno

    [env:nodemcu]
    platform = espressif8266
    framework = arduino
    board = nodemcu

    [env:teensy31]
    platform = teensy
    framework = arduino
    board = teensy31

    [env:lpmsp430g2553]
    platform = timsp430
    framework = arduino
    board = lpmsp430g2553
    build_flags = -D LED_BUILTIN=RED_LED
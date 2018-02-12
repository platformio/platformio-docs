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

.. _platform_native:

Native
======
:ref:`projectconf_env_platform` = ``native``

Native development platform is intended to be used for desktop OS. This platform uses built-in toolchains (preferable based on GCC), frameworks, libs from particular OS where it will be run.

For more detailed information please visit `vendor site <https://platformio.org/platforms/native?utm_source=platformio&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Native development platform repository <https://github.com/platformio/platform-native/tree/develop/examples?utm_source=platformio&utm_medium=docs>`_:

* `hello-world <https://github.com/platformio/platform-native/tree/develop/examples/hello-world?utm_source=platformio&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-native/releases>`__
of Native development platform and the latest upstream version using
:ref:`projectconf_env_platform` option as described below:

.. code-block:: ini

    ; Custom stable version
    [env:stable]
    platform =native@x.y.z
    board = ...
    ...

    ; The latest upstream/development version
    [env:upstream]
    platform = https://github.com/platformio/platform-native.git
    board = ...
    ...

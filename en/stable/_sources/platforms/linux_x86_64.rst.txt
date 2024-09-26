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

.. _platform_linux_x86_64:

Linux x86_64
============

:Registry:
  `https://registry.platformio.org/platforms/platformio/linux_x86_64 <https://registry.platformio.org/platforms/platformio/linux_x86_64>`__
:Configuration:
  :ref:`projectconf_env_platform` = ``platformio/linux_x86_64``

Linux x86_64 (64-bit) is a Unix-like and mostly POSIX-compliant computer operating system (OS) assembled under the model of free and open-source software development and distribution. Using host OS (Mac OS X or Linux 64-bit) you can build native application for Linux x86_64 platform.

For more detailed information please visit `vendor site <https://registry.platformio.org/platforms/platformio/linux_x86_64?utm_source=platformio.org&utm_medium=docs>`_.

.. contents:: Contents
    :local:
    :depth: 1


Examples
--------

Examples are listed from `Linux x86_64 development platform repository <https://github.com/platformio/platform-linux_x86_64/tree/master/examples?utm_source=platformio.org&utm_medium=docs>`_:

* `hello-world <https://github.com/platformio/platform-linux_x86_64/tree/master/examples/hello-world?utm_source=platformio.org&utm_medium=docs>`_

Stable and upstream versions
----------------------------

You can switch between `stable releases <https://github.com/platformio/platform-linux_x86_64/releases>`__
of Linux x86_64 development platform and the latest upstream version using
:ref:`projectconf_env_platform` option in :ref:`projectconf` as described below.

Stable
~~~~~~

.. code-block:: ini

    ; Latest stable version, NOT recommended
    ; Pin the version as shown below
    [env:latest_stable]
    platform = linux_x86_64
    
    ; Specific version
    [env:custom_stable]
    platform = linux_x86_64@x.y.z
    
Upstream
~~~~~~~~

.. code-block:: ini

    [env:upstream_develop]
    platform = https://github.com/platformio/platform-linux_x86_64.git
    

Packages
--------

.. list-table::
    :header-rows:  1

    * - Name
      - Description

    * - `toolchain-gcclinux64 <https://registry.platformio.org/tools/platformio/toolchain-gcclinux64>`__
      - GCC Toolchain for Linux x86_64 machines
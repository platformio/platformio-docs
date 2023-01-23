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

.. _projectconf_targets:

``targets``
-----------

Type: ``String`` | Multiple: ``Yes``

A list of targets which will be processed by the :ref:`cmd_run` command by
default. You can enter more than one target, if separated by comma+space **", "**.

Please follow to :option:`pio run --list-targets` documentation for the other
targets.

**Examples**

1. Build a project using :ref:`Release Configuration <build_configurations>`,
   upload the firmware, and start :ref:`Serial Monitor <cmd_device_monitor>`
   automatically:

    .. code-block:: ini

       [env:upload_and_monitor]
       targets = upload, monitor

2. Build a project using :ref:`Debug Configuration <build_configurations>`.


**Tip!** You can use these targets like an option to
:option:`pio run --target` command. For example:

.. code-block:: bash

    # clean project
    pio run -t clean

    # dump current build environment
    pio run --target envdump

When no targets are defined, *PlatformIO* will build only sources by default.
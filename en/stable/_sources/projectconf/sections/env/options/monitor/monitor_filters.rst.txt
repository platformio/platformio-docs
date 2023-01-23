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

.. _projectconf_monitor_filters:

``monitor_filters``
-------------------

Type: ``String`` | Multiple: ``Yes``

Apply filters and text transformation for device output. See available filters at
:ref:`cmd_device_monitor_filters`.

Example:

.. code-block:: ini

    [env:log_output_to_file_with_timestamp]
    ...
    platform = ...
    monitor_filters =
      default   ; Remove typical terminal control codes from input
      time      ; Add timestamp with milliseconds for each new line
      log2file  ; Log data to a file “platformio-device-monitor-*.log” located in the current working directory

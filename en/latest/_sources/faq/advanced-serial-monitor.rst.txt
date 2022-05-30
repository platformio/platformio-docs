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

.. _faq_advanced_serial_monitor_ui:

Advanced Serial Monitor with UI
-------------------------------

PlatformIO Core provides CLI version (:ref:`cmd_device_monitor`) of Serial Monitor.
If you need advanced instrument with a rich UI, we recommend free and multi-platform
`CoolTerm <https://freeware.the-meiers.org/?utm_source=platformio&utm_medium=docs>`_
serial port terminal application.

.. warning::
  Please note that you need to **manually disconnect (close serial port connection)** in
  CoolTerm **before doing uploading** in PlatformIO. PlatformIO can not disconnect/connect
  to a target device automatically when CoolTerm is used.

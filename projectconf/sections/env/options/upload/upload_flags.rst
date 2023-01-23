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

.. _projectconf_upload_flags:

``upload_flags``
----------------

Type: ``String`` | Multiple: ``Yes``

Extra flags for uploader. Will be added to the end of uploader command. If you
need to override uploader command or base flags please use
:ref:`projectconf_extra_scripts`.

This option can also be set by global environment variable
:envvar:`PLATFORMIO_UPLOAD_FLAGS`.

**Example**

Please specify each flag/option in a new line starting with minimum 2 spaces.

.. code-block:: ini

    [env:atmega328pb]
    platform = atmelavr
    board = atmega328pb
    framework = arduino
    upload_flags =
      -P$UPLOAD_PORT
      -b$UPLOAD_SPEED
      -u
      -Ulock:w:0xCF:m
      -Uhfuse:w:0xD7:m
      -Uefuse:w:0xF6:m
      -Ulfuse:w:0xE2:m

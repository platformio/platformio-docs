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

.. _projectconf_upload_protocol:

``upload_protocol``
-------------------

Type: ``String`` | Multiple: ``No``

A protocol that "uploader" tool uses to talk to a board. Please check
:ref:`boards` for supported uploading protocols by your board.

.. note::
    ``upload_protocol = custom`` allows one to use a custom ``upload_command`` - see below.

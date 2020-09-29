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

.. _board_creating:

Custom Embedded Boards
======================

*PlatformIO* has pre-built settings for many popular embedded
boards. The list of these boards is available as a web page at
`PlatformIO Boards Explorer <https://platformio.org/boards>`_ or
through the CLI command :ref:`cmd_boards`.

Custom boards can also be defined from scratch or by overriding settings
of existing boards. All data is declared using the `JSON syntax
<http://en.wikipedia.org/wiki/JSON>`_ via `associative array
<http://en.wikipedia.org/wiki/Associative_array>`_ name/value pairs.

.. contents::

JSON Structure
--------------

The key fields are:

* ``build`` data is handed over to the :ref:`platforms` and :ref:`frameworks` builders
* ``frameworks`` is the list with supported :ref:`frameworks`. Each working environment for each project that uses the board will choose one of the frameworks declared here.
* ``platform`` name of :ref:`platforms`
* ``upload`` upload settings which depend on the ``platform``

For details, see existing boards as examples, available under ``.platformio/platforms/*/boards/``.

.. code-block:: json

    {
      "build": {
        "extra_flags": "-DHELLO_PLATFORMIO",
        "f_cpu": "16000000L",
        "hwids": [
          [
            "0x1234",
            "0x0013"
          ],
          [
            "0x4567",
            "0x0013"
          ]
        ],
        "mcu": "%MCU_TYPE_HERE%"
      },
      "frameworks": ["%LIST_WITH_SUPPORTED_FRAMEWORKS%"],
      "platforms": ["%LIST_WITH_COMPATIBLE_PLATFORMS%"]
      "name": "My Test Board",
      "upload": {
        "maximum_ram_size": 2048,
        "maximum_size": 32256
      },
      "url": "http://example.com",
      "vendor": "MyCompany"
    }


Installation
------------

1. Create ``boards`` directory in :ref:`projectconf_pio_core_dir` if it
   doesn't exist.
2. Create ``myboard.json`` file in this ``boards`` directory.
3. Search available boards via :ref:`cmd_boards` command. You should see
   ``myboard`` board.

Now, you can use ``myboard`` for the :ref:`projectconf_env_board` option in
:ref:`projectconf`.

.. note::
  You can have custom boards per project. In this case, please put your
  board's JSON files to :ref:`projectconf_pio_boards_dir`.

Examples
--------

Please take a look at the source code of
`PlatformIO Development Platforms <https://github.com/platformio?query=platform->`_
and navigate to ``boards`` folder of the repository.

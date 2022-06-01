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

.. _manifest_library_json_dependencies:

``dependencies``
----------------

*Optional* | Type: ``Array`` or ``Object``

A list of dependent libraries that will be automatically installed.

Allowed requirements for dependent library:

* ``owner`` | Type: ``String`` – an owner name (username) from the `PlatformIO Registry <https://registry.platformio.org>`__
* ``name`` | Type: ``String`` – library name
* ``version`` | Type: ``String`` – :ref:`cmd_pkg_install_requirements` or :ref:`cmd_pkg_install_specifications`
* ``frameworks`` | Type: ``String`` or ``Array`` – project compatible :ref:`frameworks`
* ``platforms`` | Type: ``String`` or ``Array`` – project compatible :ref:`platforms`

**Example**

.. code-block:: javascript

    "dependencies":
    {
        "bblanchon/ArduinoJson": "^6.16.1",
        "me-no-dev/AsyncTCP": "*",
        "external-repo": "https://github.com/user/package.git#1.2.3",
        "external-zip": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
    }

More advanced usage:

.. code-block:: javascript

    "dependencies":
    [
        {
            "owner": "bblanchon",
            "name": "ArduinoJson",
            "version": "^6.16.1"
        },
        {
            "owner": "me-no-dev",
            "name": "AsyncTCP",
            "version": "*",
            "platforms": ["espressif32"]
        },
        {
            "name": "external-repo",
            "version": "https://github.com/user/package.git#1.2.3"
        },
        {
            "name": "external-zip",
            "version": "https://github.com/me-no-dev/AsyncTCP/archive/master.zip"
        }
    ]

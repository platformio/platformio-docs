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

.. _cmd_access_list:

pio access list
===============

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio access list [OPTIONS] [OWNER]

Description
-----------

Show all of the resources (packages) a user or a team can access, along with the access
level, except for read-only public resources (it won’t print the whole registry listing).

To list resources by the specified owner, type owner's "username" as an argument to this command.

See the examples below.

Options
~~~~~~~

.. program:: pio access list

.. option::
    --urn-type

Resource type in `URN <https://en.wikipedia.org/wiki/Uniform_Resource_Name>`_ form.
Default is set to ``prn:reg:pkg`` which means to list the packages from the registry.

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

1. List all accessible resources:

.. code-block:: bash

    > pio access list

    ...

    atmelsam
    --------
    URN:              prn:reg:pkg:8007:platform
    Owner:            platformio
    Access level(s):  Admin

    espressif8266
    -------------
    URN:              prn:reg:pkg:8008:platform
    Owner:            platformio
    Access level(s):  Admin

    chipsalliance
    -------------
    URN:              prn:reg:pkg:8036:platform
    Owner:            platformio
    Access level(s):  Admin

    contrib-piohome
    ---------------
    URN:              prn:reg:pkg:8037:tool
    Owner:            platformio
    Access level(s):  Admin

    contrib-pysite
    --------------
    URN:              prn:reg:pkg:8038:tool
    Owner:            platformio
    Access level(s):  Admin

    ...

2. List all accessible resources by specific owner:

.. code-block:: bash

    > pio access list platformio

    ...

    tool-scons
    ----------
    URN:              prn:reg:pkg:8192:tool
    Owner:            platformio
    Access level(s):  Admin

    tool-simavr
    -----------
    URN:              prn:reg:pkg:8193:tool
    Owner:            platformio
    Access level(s):  Admin

    ...

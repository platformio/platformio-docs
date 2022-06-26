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

.. _cmd_pkg_publish:

pio pkg publish
===============

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg publish [<source directory, tar.gz or zip>] [OPTIONS]


Description
-----------

Publish a package to the `PlatformIO Registry <https://registry.platformio.org/>`__ so that it can be installed by name.
All files in the package directory are included if ``export`` field is not declared
in a package manifest (for example, see :ref:`manifest_library_json_export`).
The `next items <https://github.com/platformio/platformio-core/blob/develop/platformio/package/pack.py>`__ are
automatically excluded.

Please check which files will be included in the final package using the
:ref:`cmd_pkg_pack` command.

Once a package is published with a given name and version, that specific name and
version combination can never be used again, even if it is removed with the
:ref:`cmd_pkg_unpublish` command.

If no arguments are supplied, then PlatformIO packs the current package folder.

To list published packages, please use the :ref:`cmd_access_list` command.

Options
-------

.. program:: pio pkg publish

.. option::
    --owner

:ref:`pioaccount` username (can be organization username). The default is set to a
username of the authorized :ref:`pioaccount`.

.. option::
    --type

Set a custom package type. See supported :ref:`cmd_pkg_install_types`.

.. option::
    --released-at

Custom release date and time in the next format (UTC): 2014-06-13 17:08:52

The permission to set custom release dates and times is only available in the `Enterprises <https://registry.platformio.org/pricing>`__ plan.

.. option::
    --private

Restrict access to a package (will not be available publicly). The default is to publish
a package publicly.

Please check `PlatformIO Registry Plans <https://registry.platformio.org/pricing>`__ where private packages are allowed.

.. option::
  --no-notify

Do not notify by email when a package is processed. The default behavior is to notify.

.. option::
  --no-interactive

Do not show an interactive prompt.

See Also
--------

* :ref:`library_json`
* :ref:`cmd_pkg_pack`
* :ref:`cmd_access_list`
* :ref:`cmd_pkg_unpublish`

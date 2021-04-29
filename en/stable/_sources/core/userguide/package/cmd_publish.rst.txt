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

.. _cmd_package_publish:

pio package publish
===================

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio package publish [<source directory, tar.gz or zip>] [OPTIONS]


Description
-----------

Publish a package to the registry so that it can be installed by name.
All files in the package directory are included if ``export`` field is not declared
in a package manifest (for example, see :ref:`libjson_export`).
The `next items <https://github.com/platformio/platformio-core/blob/develop/platformio/package/pack.py#L33>`__ are
automatically excluded.

Please check which files will be included in the final package using the
:ref:`cmd_package_pack` command.

Once a package is published with a given name and version, that specific name and
version combination can never be used again, even if it is removed with the
:ref:`cmd_package_unpublish` command.

If no arguments are supplied, then PlatformIO packs the current package folder.

To list published packages, please use :ref:`cmd_access_list` command.

Options
~~~~~~~

.. program:: pio package publish

.. option::
    --owner

:ref:`pioaccount` username (can be organization username). The default is set to a
username of the authorized :ref:`pioaccount`.

.. option::
    --released-at

Custom release date and time in the next format (UTC): 2014-06-13 17:08:52

.. option::
    --private

.. note::
    The permission to set custom release dates and times is only available to Super Admins. 

Restrict access to a package (will not be available publicly). The default is to publish
a package publicly.

.. option::
  --no-notify

Do not notify by email when package is processed. The default behavior is to notify.

See Also
--------

* :ref:`library_json`
* :ref:`cmd_package_pack`
* :ref:`cmd_package_unpublish`

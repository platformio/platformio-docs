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

.. _cmd_package_unpublish:

pio package unpublish
=====================

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio package unpublish [<organization>/]<pkgname>[@<version>] [OPTIONS]

Description
-----------

This removes a package version from the registry, deleting its entry and removing the
tarball.

If no version is specified, or if all versions are removed then the root package entry
is removed from the registry entirely.

You can only remove a package version within 72 hours since the published date.

Options
~~~~~~~

.. program:: pio package unpublish

.. option::
    --type

Set the type of a package to unpublish (if you have packages with the same name).
Possible values are ``library``, ``platform``, or ``tool``. The default is set to ``library``.

.. option::
    --undo

Undo a remove, putting a version back into the registry.

See Also
--------

* :ref:`library_json`
* :ref:`cmd_package_pack`
* :ref:`cmd_package_publish`

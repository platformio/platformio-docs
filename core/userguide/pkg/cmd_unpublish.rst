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

.. _cmd_pkg_unpublish:

pio pkg unpublish
=================

.. contents::

Usage
-----

.. code-block:: bash

    pio pkg unpublish [<organization>/]<pkgname>[@<version>] [OPTIONS]

Description
-----------

This removes a package version from the registry, deleting its entry and removing the
tarball.

If no version is specified, or if all versions are removed then the root package entry
is removed from the registry entirely.

You can only remove a package version within 72 hours from the published date.

Options
-------

.. program:: pio pkg unpublish

.. option::
    --type

Set the type of a package to unpublish (if you have packages with the same name).
The default is set to the ``library``. See supported :ref:`cmd_pkg_install_types`.

.. option::
    --undo

Undo a remove, putting a version back into the registry.

See Also
--------

* :ref:`library_json`
* :ref:`cmd_pkg_pack`
* :ref:`cmd_pkg_publish`

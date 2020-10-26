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

.. _cmd_access_private:

pio access private
==================

.. versionadded:: 5.0

.. contents::

Usage
-----

.. code-block:: bash

    pio access private [OPTIONS] URN

Description
-----------

Set a resource to be either privately accessible (restricted access to particular
users or team members).

Options
~~~~~~~

.. program:: pio access private

.. option::
    --urn-type

Resource type in `URN <https://en.wikipedia.org/wiki/Uniform_Resource_Name>`_ form.
Default is set to ``prn:reg:pkg`` which means to grant access to the package in
the registry.

Examples
--------

.. code-block:: bash

    > pio access private prn:reg:pkg:8036:platform
    The resource "prn:reg:pkg:8036:platform" has been successfully updated.

See Also
--------

* :ref:`cmd_access_public`

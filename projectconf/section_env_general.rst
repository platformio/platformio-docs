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

.. _projectconf_section_env_general:

General options
~~~~~~~~~~~~~~~

.. contents::
    :local:

.. _projectconf_env_platform:

``platform``
^^^^^^^^^^^^

:ref:`platforms` name.

PlatformIO allows to use specific version of platform using
`Semantic Versioning <http://semver.org>`_ (X.Y.Z=MAJOR.MINOR.PATCH).
Version specifications can take any of the following forms:

* ``0.1.2``: an exact version number. Use only this exact version
* ``^0.1.2``: any compatible version (exact version for ``0.x.x`` versions
* ``~0.1.2``: any version with the same major and minor versions, and an
  equal or greater patch version
* ``>0.1.2``: any version greater than ``0.1.2``. ``>=``, ``<``, and ``<=``
  are also possible
* ``>0.1.0,!=0.2.0,<0.3.0``: any version greater than ``0.1.0``, not equal to
  ``0.2.0`` and less than ``0.3.0``

Examples:

.. code-block:: ini

    [env:the_latest_version]
    platform = atmelavr

    [env:specific_major_version]
    platform = atmelavr@^0.1.2

    [env:specific_major_and_minor_version]
    platform = atmelavr@~0.1.2

.. _projectconf_env_framework:

``framework``
^^^^^^^^^^^^^

:ref:`frameworks` name.

The multiple frameworks are allowed, *split them with comma+space ", "*.

.. _projectconf_env_board:

``board``
^^^^^^^^^

*PlatformIO* has pre-configured settings for the most popular boards. You don't
need to specify ``board_mcu``, ``board_f_cpu``, ``upload_protocol`` or
``upload_speed`` options. Just define a ``board`` type and *PlatformIO* will
pre-fill options described above with appropriate values.

You can find the ``board`` type in *Boards* section of each :ref:`platforms` or
using `PlatformIO Embedded Boards Explorer <http://platformio.org/boards>`_.

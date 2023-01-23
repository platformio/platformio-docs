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

.. _projectconf_section_platformio:

Section ``[platformio]``
------------------------

.. contents::
    :local:

The ``platformio`` section in the platformio.ini file is used for overriding the
default configuration options for :ref:`piocore`.

.. note::
    Relative path is allowed for directory option:

    * ``~`` will be expanded to user's home directory
    * ``../`` or ``..\`` go up to one folder

    There is a ``$PROJECT_HASH`` template variable. You can use it in a directory
    path. It will by replaced by a SHA1[0:10] hash of the full project path.
    This is very useful to declare a global storage for project workspaces.
    For example, ``/tmp/pio-workspaces/$PROJECT_HASH`` (Unix) or
    ``$[sysenv.TEMP}/pio-workspaces/$PROJECT_HASH`` (Windows).
    You can set a global workspace directory using the system environment
    variable :envvar:`PLATFORMIO_WORKSPACE_DIR`.

    See the available directory ``***_dir`` options below.

.. toctree::
    :maxdepth: 2

    options/generic/index
    options/directory/index

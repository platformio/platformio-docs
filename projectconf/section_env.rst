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

.. _projectconf_section_env:

Section ``[env:NAME]``
----------------------

.. contents::
    :local:

A section with ``env:`` prefix is used to define virtual environment with
specific options that will be processed with :ref:`cmd_run` command. You can
define unlimited numbers of environments.

Each environment must have unique ``NAME``. The valid chars for ``NAME`` are

* letters ``a-z``
* numbers ``0-9``
* special char ``_`` (underscore)

For example, ``[env:hello_world]``.

.. toctree::
    :maxdepth: 2

    section_env_general
    section_env_board
    section_env_build
    section_env_upload
    section_env_monitor
    section_env_library
    section_env_test
    section_env_debug
    section_env_advanced

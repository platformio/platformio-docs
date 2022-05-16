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

.. _scripting:

Advanced Scripting
==================

.. warning::
  Advanced Scripting is recommended for Advanced Users and requires
  knowledge of the Python language.

The PlatformIO Build System allows the user to extend the build process with
custom scripts using the Python interpreter and
the `SCons <http://www.scons.org>`_ construction tool.
Build flags, upload flags, targets, toolchains data and other information are
available for modification as `SCons Construction Environments <http://www.scons.org/doc/production/HTML/scons-user.html#chap-environments>`_.
Custom scripts are included with :ref:`projectconf_extra_scripts`.

.. warning::
  Please note that you can not run or debug these scripts independently
  with Python interpreter. They will be loaded automatically when the
  :ref:`cmd_run` command processes the project environment.

.. toctree::
  :maxdepth: 2

  launch_types
  construction_environments
  actions
  middlewares
  custom_targets
  Examples <examples/index>
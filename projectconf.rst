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

.. _projectconf:

Project Configuration File ``platformio.ini``
=============================================

The Project configuration file is named ``platformio.ini``. This is a
`INI-style <http://en.wikipedia.org/wiki/INI_file>`_ file.

``platformio.ini`` has sections (each denoted by a ``[header]``) and
key / value pairs within the sections. Lines beginning with ``;``
are ignored and may be used to provide comments.

There are 2 system reserved sections:

* Base PlatformIO settings: :ref:`projectconf_section_platformio`
* Build Environment settings: :ref:`projectconf_section_env`

The other sections can be used by users, for example, for
:ref:`projectconf_dynamic_vars`. The sections and their allowable values are
described below.

.. toctree::
    :maxdepth: 2

    projectconf/section_platformio
    projectconf/section_env
    projectconf/dynamic_variables
    projectconf/examples

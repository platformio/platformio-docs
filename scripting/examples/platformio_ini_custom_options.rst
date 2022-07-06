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

.. _scripting_example_custom_project_conf_options:

Custom options in ``platformio.ini``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PlatformIO allows you extending project configuration with own data.
Custom options have to start with ``custom_`` or ``board_`` to not generate a warning that
the unknown configuration option will be ignored by PlatformIO.
You can read these values later using `ProjectConfig API <https://github.com/platformio/platformio-core/blob/develop/platformio/project/config.py>`__:

:``ProjectConfig::get(section, option, default=None)``:
    Get an option value for the named section

:``ProjectConfig::options(section)``:
    Returns a list of the sections available

:``ProjectConfig::items(section, as_dict=False)``:
    Returns a list of "name", "value" pairs for the options in the given section or a dictionary when ``as_dict=True`` is passed

:``ProjectConfig::has_section(section)``:
    Indicates whether the named section is present in the configuration

:``ProjectConfig::has_option(section, option)``:
    If the given section exists, and contains the given option, returns ``True``; otherwise returns ``False``.

PlatformIO's "ProjectConfig" is compatible with a native Python's `ConfigParser <https://docs.python.org/3/library/configparser.html>`__ API.

**Example**

``platformio.ini``:

.. code-block:: ini

    [universe]
    hello = world

    [env:my_env]
    platform = ...
    extra_scripts = extra_script.py

    custom_option1 = value1
    custom_option2 = value2

``extra_script.py``:

.. code-block:: python

    # "env.GetProjectOption" shortcut for the active environment
    value1 = env.GetProjectOption("custom_option1")
    value2 = env.GetProjectOption("custom_option2")

    # Read value from other environments
    config = env.GetProjectConfig()
    world = config.get("universe", "hello")
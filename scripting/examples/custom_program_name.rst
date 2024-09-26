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

Custom firmware/program name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sometimes it is useful to have a different firmware/program name in
:ref:`projectconf_pio_build_dir`. The following example uses
:ref:`scripting_example_custom_project_conf_options` and adds
a project version suffix to the firmware name.

``platformio.ini``:

.. code-block:: ini

    [env:env_custom_prog_name]
    platform = platformio/espressif32
    framework = arduino
    board = esp32dev
    build_flags =
        -DVERSION=${this.custom_prog_version}
    extra_scripts = pre:extra_script.py
    custom_prog_version = 1.2.3

``extra_script.py``:

.. code-block:: python

    Import("env")

    env.Replace(PROGNAME="firmware_%s" % env.GetProjectOption("custom_prog_version"))

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

Build external sources
^^^^^^^^^^^^^^^^^^^^^^

If your project depends on some arbitrary source files that are located outside of the
usual source directory :ref:`projectconf_pio_src_dir` then you can use a preliminary
extra script to add them to the build process. A typical situation when this approach
may be useful is when a project depends on pregenerated files in a temporary folder.
Here is a typical configuration with an extra_script that instructs PlatformIO to build
all sources in an external folder:

``platformio.ini``:

.. code-block:: ini

    [env:my_env]
    platform = ...
    extra_scripts = pre:extra_script.py

``extra_script.py`` (place it near ``platformio.ini``):

.. code-block:: python

    import os

    Import("env")

    env.BuildSources(
        os.path.join("$BUILD_DIR", "external", "build"),
        os.path.join("$PROJECT_DIR", "external", "sources")
    )
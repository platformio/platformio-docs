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

.. _projectconf_pio_src_dir:

``src_dir``
-----------

Type: ``DirPath`` | Multiple: ``No`` | Default: "<Project>/``src``"

The ``src_dir`` is the path to the directory where the source code of
the project is located. It is used by the :ref:`cmd_run` command to compile
and upload the code to the device. By default, the ``src_dir`` is set to ``src``,
which means the source code is located in a directory named ``src``
in the root directory of the project.

You can customize the base directory by setting the :envvar:`PLATFORMIO_SRC_DIR`
environment variable. This variable should contain the absolute path to the
directory where the source code is located.

.. hint::

    To include or exclude specific source files from the build process, use the
    :ref:`projectconf_build_src_filter` option in the :ref:`projectconf`.
    The :ref:`projectconf_build_src_filter` option can take a list of file patterns
    in glob syntax. Only the source files that match the specified patterns will be included in the build process.

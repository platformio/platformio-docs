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

.. _installation_installer_script:

Installer Script (Recommended)
------------------------------

.. warning::
    PlatformIO operates **without the need for administrative or sudo permissions**.
    It is strongly advised to perform the installation using the default user
    account and without any additional permissions. This approach ensures a smooth
    installation process and helps maintain a secure and controlled environment.

.. note::
    To facilitate the integration of PlatformIO Core with :ref:`ci` systems and
    containers, we highly recommend installing PlatformIO Core directly from
    the :ref:`installation_pypi`. This method is not only the fastest but
    also the most straightforward way to ensure a seamless setup.

Install PlatformIO Core into the Virtual Python Environment using the
`Installer Script <https://github.com/platformio/platformio-core-installer>`_.

A default location of Python virtual environment is ":ref:`projectconf_pio_core_dir`/penv".
If you have any issues with PlatformIO Core, just remove this folder and re-run
installer script.

.. contents::
    :local:

Super-Quick (macOS / Linux)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install or upgrade PlatformIO Core paste that at a *Terminal* prompt:

Using ``curl``

.. code-block:: bash

    curl -fsSL -o get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
    python3 get-platformio.py

or using ``wget``

.. code-block:: bash

    wget -O get-platformio.py https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py
    python3 get-platformio.py


Local Download (macOS / Linux / Windows)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To install or upgrade PlatformIO Core, download (save as...)
`get-platformio.py <https://raw.githubusercontent.com/platformio/platformio-core-installer/master/get-platformio.py>`__
script. Then run the following:

.. code-block:: bash

    # change directory to the folder where is located downloaded "get-platformio.py"
    cd /path-to-dir/where/get-platformio.py/is-located

    # run it
    python get-platformio.py


On *Windows OS* it may look like this:

.. code-block:: bash

    # change directory to the folder where is located downloaded "get-platformio.py"
    cd C:/path-to-dir/where/get-platformio.py/is-located

    # run it
    python.exe get-platformio.py

.. note::
    If you need to have access to ``pio`` or ``pio.exe`` commands from
    other applications or terminals in your OS, please :ref:`piocore_install_shell_commands`.

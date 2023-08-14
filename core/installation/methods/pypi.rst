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

.. _installation_pypi:

Python Package Manager
----------------------

.. warning::
    It's best to stick with this method **ONLY IF** you're dealing with :ref:`ci`
    systems/containers or if you have complete permissions to set up
    PlatformIO Core across your entire operating system.

    For your own personal use, and to steer clear of troubles when it comes to
    maintenance and updates, we **STRONGLY SUGGEST** going for the
    :ref:`installation_installer_script`. This script installs PlatformIO Core
    in a separate virtual environment, keeping it isolated from your operating
    system and avoiding any impact on it.

The latest stable version of PlatformIO Core may be installed or upgraded via
Python Package Manager (`pip <https://pip.pypa.io>`_) as follows:

.. code-block:: bash

    python3 -m pip install -U platformio

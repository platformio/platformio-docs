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

.. _piocore_uninstall:

Uninstall PlatformIO Core and dependent packages
------------------------------------------------

* The isolated installation of PlatformIO Core and dependent packages
  are installed to the :ref:`projectconf_pio_core_dir` folder. Just remove it.

* Uninstall global PlatformIO Core if you did not use the :ref:`installation_installer_script`:

    .. code-block:: bash

        # uninstall standalone PlatformIO Core installed via `pip`
        pip uninstall platformio
        python -m pip uninstall platformio

        # uninstall Homebrew's PlatformIO Core (only macOS users if you installed it via Homebrew before)
        brew uninstall platformio

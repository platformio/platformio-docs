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

.. _installation_develop:

Development Version
-------------------

.. warning::
    If you use :ref:`pioide`, please enable development version and restart IDE:

    * :ref:`ide_vscode`: Set ``platformio-ide.useDevelopmentPIOCore`` to ``true`` in
      :ref:`ide_vscode_settings`.

Install the latest PlatformIO from the ``develop`` branch:

.. code-block:: bash

    python -m pip install -U https://github.com/platformio/platformio-core/archive/develop.zip

If you want to be up-to-date with the latest ``develop`` version of PlatformIO,
then you need to re-install PlatformIO each time you see a new commit in
`PlatformIO GitHub repository (branch: develop) <https://github.com/platformio/platformio-core/commits/develop>`_ like so:

.. code-block:: bash

    python -m pip install -U https://github.com/platformio/platformio-core/archive/develop.zip

Or:

.. code-block:: bash

    pio upgrade --dev

To revert to the latest stable version:

.. code-block:: bash

    python -m pip uninstall platformio
    python -m pip install -U platformio

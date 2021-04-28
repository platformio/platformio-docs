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

.. _cmd_settings:

pio settings
============

Manage PlatformIO settings

.. contents::

.. _cmd_settings_get:

pio settings get
----------------

Usage
~~~~~

.. code-block:: bash

    pio settings get [NAME]


Description
~~~~~~~~~~~

.. note::
    * The ``Yes`` value is equal to: ``True``, ``Y``, ``1`` and is not case sensitive.
    * You can override these settings using :ref:`envvars`.

Get/List existing settings

Settings
~~~~~~~~

.. _setting_auto_update_libraries:

``auto_update_libraries``
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   No
:Values:    Yes/No

Automatically update libraries.

.. _setting_auto_update_platforms:

``auto_update_platforms``
^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   No
:Values:    Yes/No

Automatically update platforms.

.. _setting_check_libraries_interval:

``check_libraries_interval``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   7
:Values:    Days (Number)

Check for the library updates interval.

.. _setting_check_platformio_interval:

``check_platformio_interval``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   3
:Values:    Days (Number)

Check for the new PlatformIO interval.

.. _setting_check_platforms_interval:

``check_platforms_interval``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   7
:Values:    Days (Number)

Check for the platform updates interval.

.. _setting_check_prune_system_threshold:

``check_prune_system_threshold``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Default:   1024
:Values:    Megabytes (Number)

Check for pruning unnecessary data threshold (megabytes). You can list unnecessary
PlatformIO system data using :option:`pio system prune --dry-run` command. See
:ref:`cmd_system_prune` for the other options.

Do disable checking for unnecessary data, please set threshold to ``0`` using
:ref:`cmd_settings_set` command.

.. _setting_enable_cache:

``enable_cache``
^^^^^^^^^^^^^^^^

:Default:   Yes
:Values:    Yes/No

Enable caching for API requests and Library Manager

.. _setting_enable_telemetry:

``enable_telemetry``
^^^^^^^^^^^^^^^^^^^^

:Default:   Yes
:Values:    Yes/No

Share minimal diagnostics and usage information to help us make PlatformIO better.

The source code of telemetry service is `open source <https://github.com/platformio/platformio-core/blob/develop/platformio/telemetry.py>`_.
You can make sure that we **DO NOT SHARE PRIVATE** information or
source code of your project. All information shares **ANONYMOUSLY**.

Which data do we collect and why?

* **A version of Python Interpreter**. :ref:`piocore` is written in `Python language <https://www.python.org/>`__,
  including development :ref:`platforms`. We need to know which Python version produces
  such type of exceptions (see below), which is more popular, which version we should
  drop and focus on a new one
* :ref:`piocore` **errors/exceptions**. We report automatically fatal exceptions raised
  by `PlatformIO Core source code <https://github.com/platformio/platformio-core>`__ but NOT by your project
* **The name of the used platform, board, framework**. We collect this type of information
  to have a clear picture which software products are the most widely used by our
  Community and for the which we should provide frequent updates and add new features (
  for example, "atmelavr", "arduino", "uno", etc.)
* **The name of CLI command**. It helps us to improve our CLI. For example, "run",
  "lib list")
* The name of :ref:`ide`. This is very important information for us. We create native
  extensions based on the popularity of IDEs (for example, :ref:`ide_vscode`, :ref:`ide_clion`)

**Thanks a lot that you keep this setting enabled!**

.. _setting_force_verbose:

``force_verbose``
^^^^^^^^^^^^^^^^^

:Default:   No
:Values:    Yes/No

Force verbose output when processing environments. This setting overrides

* :option:`pio run --verbose`
* :option:`pio ci --verbose`
* :option:`pio test --verbose`

.. _setting_projects_dir:

``projects_dir``
^^^^^^^^^^^^^^^^

:Default:   ~/Documents/PlatformIO/Projects
:Values:    Path to folder

Default location for PlatformIO projects (PlatformIO Home)

Examples
~~~~~~~~

1. List all settings and theirs current values

.. code::

    > pio settings get

    Name                            Value [Default]   Description
    ------------------------------------------------------------------------------------------
    auto_update_libraries           No                Automatically update libraries (Yes/No)
    auto_update_platforms           No                Automatically update platforms (Yes/No)
    check_libraries_interval        7                 Check for the library updates interval (days)
    check_platformio_interval       3                 Check for the new PlatformIO interval (days)
    check_platforms_interval        7                 Check for the platform updates interval (days)
    check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
    enable_cache                    Yes               Enable caching for API requests and Library Manager
    strict_ssl                      No                Strict SSL for PlatformIO Services
    enable_telemetry                Yes               Telemetry service?#enable-telemetry> (Yes/No)
    force_verbose                   No                Force verbose output when processing environments
    projects_dir                    ~/Documents/PlatformIO/Projects Default location for PlatformIO projects (PlatformIO Home)


2. Show specified setting

.. code-block:: bash

    > pio settings get auto_update_platforms
    Name                            Value [Default]   Description
    ------------------------------------------------------------------------------------------
    auto_update_platforms           Yes               Automatically update platforms (Yes/No)

.. _cmd_settings_set:

pio settings set
----------------

Usage
~~~~~

.. code-block:: bash

    pio settings set NAME VALUE


Description
~~~~~~~~~~~

Set new value for the setting

Examples
~~~~~~~~

Change to check for the new PlatformIO each day

.. code-block:: bash

    > pio settings set check_platformio_interval 1
    The new value for the setting has been set!
    Name                            Value [Default]   Description
    ------------------------------------------------------------------------------------------
    check_platformio_interval       1 [3]             Check for the new PlatformIO interval (days)


.. _cmd_settings_reset:

pio settings reset
------------------

Usage
~~~~~

.. code-block:: bash

    pio settings reset


Description
~~~~~~~~~~~

Reset settings to default

Examples
~~~~~~~~

.. code-block:: bash

    > pio settings reset
    The settings have been reset!

    Name                            Value [Default]   Description
    ------------------------------------------------------------------------------------------
    auto_update_libraries           No                Automatically update libraries (Yes/No)
    auto_update_platforms           No                Automatically update platforms (Yes/No)
    check_libraries_interval        7                 Check for the library updates interval (days)
    check_platformio_interval       3                 Check for the new PlatformIO interval (days)
    check_platforms_interval        7                 Check for the platform updates interval (days)
    check_prune_system_threshold    1024              Check for pruning unnecessary data threshold (megabytes)
    enable_cache                    Yes               Enable caching for API requests and Library Manager
    strict_ssl                      No                Enable SSL for PlatformIO Services
    enable_telemetry                Yes               Telemetry service?#enable-telemetry> (Yes/No)
    force_verbose                   No                Force verbose output when processing environments
    projects_dir                    ~/Documents/PlatformIO/Projects Default location for PlatformIO projects (PlatformIO Home)

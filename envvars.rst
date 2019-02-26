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

.. _envvars:

Environment variables
=====================

`Environment variables <http://en.wikipedia.org/wiki/Environment_variable>`_
are a set of dynamic named values that can affect the way running processes
will behave on a computer.

*PlatformIO* handles variables which start with ``PLATFORMIO_`` prefix. They
have the **HIGHEST PRIORITY**.

How to set environment variable?

.. code-block:: bash

    # Windows
    set VARIABLE_NAME=VALUE

    # Unix (bash, zsh)
    export VARIABLE_NAME=VALUE

    # Unix (fish)
    set -x VARIABLE_NAME VALUE

.. contents:: Contents
    :local:

General
-------

PlatformIO uses *General* environment variables for the common
operations/commands.

.. envvar:: CI

PlatformIO handles ``CI`` variable which is setup by
`Continuous Integration <http://en.wikipedia.org/wiki/Continuous_integration>`_
(Travis, Circle and etc.) systems.
PlatformIO uses it to disable prompts and progress bars. In other words,
``CI=true`` automatically setup :envvar:`PLATFORMIO_DISABLE_PROGRESSBAR` to
``true``.

.. envvar:: PLATFORMIO_AUTH_TOKEN

Allows one to specify Personal Authentication Token that could be used for
automatic login in to :ref:`pioaccount`. It is very useful for :ref:`ci`
systems and :ref:`pioremote` operations where you are not able manually authorize.

You can get own Personal Authentication Token using :ref:`cmd_account_token`
command.

.. envvar:: PLATFORMIO_FORCE_COLOR

Force to output color ANSI-codes even if the output is a ``pipe`` (not a ``tty``).
The possible values are ``true`` and ``false``. Default is ``PLATFORMIO_FORCE_COLOR=false``.

.. envvar:: PLATFORMIO_DISABLE_PROGRESSBAR

Disable progress bar for package/library downloader and uploader. This is
useful when calling PlatformIO from subprocess and output is a ``pipe`` (not a ``tty``).
The possible values are ``true`` and ``false``. Default is ``PLATFORMIO_DISABLE_PROGRESSBAR=false``.

.. envvar:: PLATFORMIO_HOME_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_home_dir`.

.. envvar:: PLATFORMIO_INCLUDE_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_include_dir`.

.. envvar:: PLATFORMIO_SRC_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_src_dir`.

.. envvar:: PLATFORMIO_LIB_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_lib_dir`.

.. envvar:: PLATFORMIO_LIBDEPS_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_libdeps_dir`.

.. envvar:: PLATFORMIO_BUILD_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_build_dir`.

.. envvar:: PLATFORMIO_DATA_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_data_dir`.

.. envvar:: PLATFORMIO_TEST_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_test_dir`.

.. envvar:: PLATFORMIO_BOARDS_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_boards_dir`.

.. envvar:: PLATFORMIO_REMOTE_AGENT_DIR

Allows one to override :option:`platformio remote agent start --working-dir`.

Building
--------

.. envvar:: PLATFORMIO_BUILD_FLAGS

Allows one to set :ref:`projectconf` option :ref:`projectconf_build_flags`.

Examples:

.. code-block:: bash

    # Unix:
    export PLATFORMIO_BUILD_FLAGS=-DFOO
    export PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -DFLOAT_VALUE=1.23457e+07
    export PLATFORMIO_BUILD_FLAGS='-DWIFI_PASS=\"My password\"' '-DWIFI_SSID=\"My ssid name\"'

    # Windows:
    SET PLATFORMIO_BUILD_FLAGS=-DFOO
    SET PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -DFLOAT_VALUE=1.23457e+07
    SET PLATFORMIO_BUILD_FLAGS='-DWIFI_PASS="My password"' '-DWIFI_SSID="My ssid name"'

.. envvar:: PLATFORMIO_SRC_BUILD_FLAGS

Allows one to set :ref:`projectconf` option :ref:`projectconf_src_build_flags`.

.. envvar:: PLATFORMIO_SRC_FILTER

Allows one to set :ref:`projectconf` option :ref:`projectconf_src_filter`.

.. envvar:: PLATFORMIO_EXTRA_SCRIPTS

Allows one to set :ref:`projectconf` option :ref:`projectconf_extra_scripts`.

.. envvar:: PLATFORMIO_LIB_EXTRA_DIRS

Allows one to set :ref:`projectconf` option :ref:`projectconf_lib_extra_dirs`.


Uploading
---------

.. envvar:: PLATFORMIO_UPLOAD_PORT

Allows one to set :ref:`projectconf` option :ref:`projectconf_upload_port`.

.. envvar:: PLATFORMIO_UPLOAD_FLAGS

Allows one to set :ref:`projectconf` option :ref:`projectconf_upload_flags`.


Settings
--------

Allows one to override PlatformIO settings. You can manage them via
:ref:`cmd_settings` command.

.. envvar:: PLATFORMIO_SETTING_AUTO_UPDATE_LIBRARIES

Allows one to override setting :ref:`setting_auto_update_libraries`.

.. envvar:: PLATFORMIO_SETTING_AUTO_UPDATE_PLATFORMS

Allows one to override setting :ref:`setting_auto_update_platforms`.

.. envvar:: PLATFORMIO_SETTING_CHECK_LIBRARIES_INTERVAL

Allows one to override setting :ref:`setting_check_libraries_interval`.

.. envvar:: PLATFORMIO_SETTING_CHECK_PLATFORMIO_INTERVAL

Allows one to override setting :ref:`setting_check_platformio_interval`.

.. envvar:: PLATFORMIO_SETTING_CHECK_PLATFORMS_INTERVAL

Allows one to override setting :ref:`setting_check_platforms_interval`.

.. envvar:: PLATFORMIO_SETTING_ENABLE_CACHE

Allows one to override setting :ref:`setting_enable_cache`.

.. envvar:: PLATFORMIO_SETTING_ENABLE_SSL

Allows one to override setting :ref:`setting_enable_ssl`.

.. envvar:: PLATFORMIO_SETTING_ENABLE_TELEMETRY

Allows one to override setting :ref:`setting_enable_telemetry`.

.. envvar:: PLATFORMIO_SETTING_FORCE_VERBOSE

Allows one to override setting :ref:`setting_force_verbose`.

.. envvar:: PLATFORMIO_SETTING_PROJECTS_DIR

Allows one to override setting :ref:`setting_projects_dir`.

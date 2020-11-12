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
will behave on a computer. PlatformIO handles variables which start with
``PLATFORMIO_`` prefix.

How to set environment variable?

.. code-block:: bash

    # Windows
    set VARIABLE_NAME=VALUE

    # Windows GUI -> https://www.youtube.com/watch?v=bEroNNzqlF4

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

.. envvar:: PLATFORMIO_FORCE_ANSI

Force to output ANSI control character even if the output is a ``pipe`` (not a ``tty``).
The possible values are ``true`` and ``false``. Default is ``PLATFORMIO_FORCE_ANSI=false``.

.. envvar:: PLATFORMIO_NO_ANSI

Do not print ANSI control characters.
The possible values are ``true`` and ``false``. Default is ``PLATFORMIO_NO_ANSI=false``.

You can also use :option:`pio --no-ansi` flag for :ref:`piocore`.

.. envvar:: PLATFORMIO_DISABLE_PROGRESSBAR

Disable progress bar for package/library downloader and uploader. This is
useful when calling PlatformIO from subprocess and output is a ``pipe`` (not a ``tty``).
The possible values are ``true`` and ``false``. Default is ``PLATFORMIO_DISABLE_PROGRESSBAR=false``.

Directories
-----------

.. envvar:: PLATFORMIO_CORE_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_core_dir`.

It may need to re-install :ref:`piocore` (remove default core directory) to take effect.

.. envvar:: PLATFORMIO_GLOBALLIB_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_globallib_dir`.

.. envvar:: PLATFORMIO_PLATFORMS_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_platforms_dir`.

.. envvar:: PLATFORMIO_PACKAGES_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_packages_dir`.

.. envvar:: PLATFORMIO_CACHE_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_cache_dir`.

.. envvar:: PLATFORMIO_BUILD_CACHE_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_build_cache_dir`.

.. envvar:: PLATFORMIO_WORKSPACE_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_workspace_dir`.

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

.. envvar:: PLATFORMIO_SHARED_DIR

Allows one to override :ref:`projectconf` option :ref:`projectconf_pio_shared_dir`.

.. envvar:: PLATFORMIO_REMOTE_AGENT_DIR

Allows one to override :option:`pio remote agent start --working-dir`.

.. envvar:: PLATFORMIO_LIB_EXTRA_DIRS

Allows one to set :ref:`projectconf` option :ref:`projectconf_lib_extra_dirs`.

Building
--------

.. envvar:: PLATFORMIO_BUILD_FLAGS

Allows one to set :ref:`projectconf` option :ref:`projectconf_build_flags`.

Examples:

.. code-block:: bash

    # Unix:
    export PLATFORMIO_BUILD_FLAGS=-DFOO
    export PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -Wall

    # Windows:
    SET PLATFORMIO_BUILD_FLAGS=-DFOO
    SET PLATFORMIO_BUILD_FLAGS=-DFOO -DBAR=1 -Wall

.. warning::

    Consider using :ref:`projectconf_dynamic_vars` instead of ``PLATFORMIO_BUILD_FLAGS``
    environment variable if additional build flags contain preprocessor directive with
    special characters (``$``, ``&``, ``~``, etc) in its value.

.. envvar:: PLATFORMIO_SRC_BUILD_FLAGS

Allows one to set :ref:`projectconf` option :ref:`projectconf_src_build_flags`.

.. envvar:: PLATFORMIO_SRC_FILTER

Allows one to set :ref:`projectconf` option :ref:`projectconf_src_filter`.

.. envvar:: PLATFORMIO_EXTRA_SCRIPTS

Allows one to set :ref:`projectconf` option :ref:`projectconf_extra_scripts`.

.. envvar:: PLATFORMIO_DEFAULT_ENVS

Allows one to set :ref:`projectconf` option :ref:`projectconf_pio_default_envs`.

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

.. envvar:: PLATFORMIO_SETTING_ENABLE_TELEMETRY

Allows one to override setting :ref:`setting_enable_telemetry`.

.. envvar:: PLATFORMIO_SETTING_FORCE_VERBOSE

Allows one to override setting :ref:`setting_force_verbose`.

.. envvar:: PLATFORMIO_SETTING_PROJECTS_DIR

Allows one to override setting :ref:`setting_projects_dir`.

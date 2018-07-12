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

.. _platform_creating:

Custom Development Platform
===========================

*PlatformIO* was developed like a tool that may build the same source code
for the different development platforms via single command :ref:`cmd_run`
without any dependent software or requirements.

For this purpose *PlatformIO* uses own pre-configured platforms data:
build scripts, toolchains, the settings for the most popular embedded
boards and etc. These data are pre-built and packaged to the different
``packages``. It allows *PlatformIO* to have multiple development platforms
which can use the same packages(toolchains, frameworks), but have
different/own build scripts, uploader and etc.

.. note::
    If you want to change some build flags for the existing
    :ref:`platforms`, you don't need to create (or duplicate) own
    development platforms! Please use :ref:`projectconf_build_flags` option.

**Step-by-Step Manual**

1. Choose :ref:`platform_creating_packages` for platform
2. Create :ref:`platform_creating_manifest_file`
3. Create :ref:`platform_creating_build_script`
4. Finish with the :ref:`platform_creating_installation`.

.. contents::

.. _platform_creating_packages:

Packages
--------

PlatformIO has own registry with pre-built packages for the most popular
systems and you can use them in your manifest. These packages are stored in
super-fast and reliably CDN storage provided by JFrog Bintray:

- https://bintray.com/platformio/dl-packages

.. _platform_creating_manifest_file:

Manifest File ``platform.json``
-------------------------------

See example with a manifest for packages:

- http://dl.platformio.org/packages/manifest.json

.. code-block:: json

    {
      "name": "myplatform",
      "title": "My Platform",
      "description": "My custom development platform",
      "url": "http://example.com",
      "homepage": "https://platformio.org/platforms/myplatform",
      "license": "Apache-2.0",
      "engines": {
        "platformio": "~3.0.0"
      },
      "repository": {
        "type": "git",
        "url": "https://github.com/platformio/platform-myplatform.git"
      },
      "version": "0.0.0",
      "packageRepositories": [
        "https://dl.bintray.com/platformio/dl-packages/manifest.json",
        "http://dl.platformio.org/packages/manifest.json",
        {
          "my_custom_package": [
            {
              "url": "http://dl.example.com/my_custom_package-darwin_x86_64-1.2.3.tar.gz",
              "sha1": "bb7ddac56a314b5cb1926cc1790ae4de3a03e65c",
              "version": "1.2.3",
              "system": [
                  "darwin_x86_64",
                  "darwin_i386"
              ]
            },
            {
              "url": "http://dl.example.com/my_custom_package-linux_aarch64-1.2.3.tar.gz",
              "sha1": "127ddac56a314b5cb1926cc1790ae4de3a03e65c",
              "version": "1.2.3",
              "system": "linux_aarch64"
            }
          ],
          "framework-%FRAMEWORK_NAME_1%": [
            {
              "url": "http://dl.example.com/packages/framework-%FRAMEWORK_NAME_1%-1.10607.0.tar.gz",
              "sha1": "adce2cd30a830d71cb6572575bf08461b7b73c07",
              "version": "1.10607.0",
              "system": "*"
            }
          ]
        }
      ],
      "frameworks": {
        "%FRAMEWORK_NAME_1%": {
          "package": "framework-%FRAMEWORK_NAME_1%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_1%.py"
        },
        "%FRAMEWORK_NAME_N%": {
          "package": "framework-%FRAMEWORK_NAME_N%",
          "script": "builder/frameworks/%FRAMEWORK_NAME_N%.py"
        }
      },
      "packages": {
        "toolchain-gccarmnoneeabi": {
          "type": "toolchain",
          "version": ">=1.40803.0,<1.40805.0"
        },
        "framework-%FRAMEWORK_NAME_1%": {
          "type": "framework",
          "optional": true,
          "version": "~1.10607.0"
        },
        "framework-%FRAMEWORK_NAME_N%": {
          "type": "framework",
          "optional": true,
          "version": "~1.117.0"
        },
        "tool-direct-vcs-url": {
          "type": "uploader",
          "optional": true,
          "version": "https://github.com/user/repo.git"
        }
      }
    }

.. _platform_creating_build_script:

Build Script ``main.py``
------------------------

Platform's build script is based on a next-generation build tool named
`SCons <http://www.scons.org>`_. PlatformIO has own built-in firmware builder
``env.BuildProgram`` with the deep libraries search. Please look into a
base template of ``main.py``.

.. code-block:: python

    """
        Build script for test.py
        test-builder.py
    """

    from os.path import join
    from SCons.Script import AlwaysBuild, Builder, Default, DefaultEnvironment

    env = DefaultEnvironment()

    # A full list with the available variables
    # http://www.scons.org/doc/production/HTML/scons-user.html#app-variables
    env.Replace(
        AR="ar",
        AS="gcc",
        CC="gcc",
        CXX="g++",
        OBJCOPY="objcopy",
        RANLIB="ranlib",

        ARFLAGS=["..."],

        ASFLAGS=["flag1", "flag2", "flagN"],
        CCFLAGS=["flag1", "flag2", "flagN"],
        CXXFLAGS=["flag1", "flag2", "flagN"],
        LINKFLAGS=["flag1", "flag2", "flagN"],

        CPPDEFINES=["DEFINE_1", "DEFINE=2", "DEFINE_N"],

        LIBS=["additional", "libs", "here"],

        UPLOADER=join("$PIOPACKAGES_DIR", "tool-bar", "uploader"),
        UPLOADCMD="$UPLOADER $SOURCES"
    )

    env.Append(
        BUILDERS=dict(
            ElfToBin=Builder(
                action=" ".join([
                    "$OBJCOPY",
                    "-O",
                    "binary",
                    "$SOURCES",
                    "$TARGET"]),
                suffix=".bin"
            )
        )
    )

    # The source code of "platformio-build-tool" is here
    # https://github.com/platformio/platformio-core/blob/develop/platformio/builder/tools/platformio.py

    #
    # Target: Build executable and linkable firmware
    #
    target_elf = env.BuildProgram()

    #
    # Target: Build the .bin file
    #
    target_bin = env.ElfToBin(join("$BUILD_DIR", "firmware"), target_elf)

    #
    # Target: Upload firmware
    #
    upload = env.Alias(["upload"], target_bin, "$UPLOADCMD")
    AlwaysBuild(upload)

    #
    # Target: Define targets
    #
    Default(target_bin)


.. _platform_creating_installation:

Installation
------------

1. Create ``platforms`` directory in :ref:`projectconf_pio_home_dir` if it
   doesn't exist.
2. Create ``myplatform`` directory in ``platforms``
3. Copy ``platform.json`` and ``builder/main.py`` files to ``myplatform`` directory.
4. Search available platforms via :ref:`cmd_platform_search` command. You
   should see ``myplatform`` platform.
5. Install ``myplatform`` platform via :ref:`cmd_platform_install` command.

Now, you can use ``myplatform`` for the :ref:`projectconf_env_platform`
option in :ref:`projectconf`.

Examples
--------

Please take a look at the source code of
`PlatformIO Development Platforms <https://github.com/platformio?query=platform->`_.

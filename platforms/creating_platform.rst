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

Custom Development Platforms
============================

*PlatformIO* can build the same binary code under
different host systems via the single command :ref:`cmd_run`
without any dependent software or requirements.

A *manifest* describes how to produce binaries for a particular
platform under one or multiple host systems by a set of build scripts,
toolchains, the settings for the most popular embedded boards, etc.

This guide explains how to write manifests, to support building for
new development platforms.


**Step-by-Step Manual**

1. Choose :ref:`platform_creating_packages` for platform
2. Create :ref:`platform_creating_manifest_file`
3. Create :ref:`platform_creating_build_script`
4. Finish with the :ref:`platform_creating_installation`.

.. contents::

.. _platform_creating_packages:

Packages
--------

Some tools are the same when compiling for several platforms, for
example a common compiler. A *package* is some tool or framework that
can be used when compiling for one or multiple platforms. Even if
multiple platforms use the same package, the package only needs to be
downloaded once. Since each package is pre-built for the different
host systems (Windows, Mac, Linux), developers can get started without
first compiling the tools.

PlatformIO has a registry with pre-built packages for the most popular
operating systems and you can use them in your platform
manifest. These packages are stored in the super-fast and reliably CDN
storage provided by `JFrog Bintray
<https://bintray.com/platformio/dl-packages>`_.

Each platform definition must define ``packageRepositories`` to link
to *package manifest files* that lists how PlatformIO can download the
used packages. To use the pre-built packages, include
http://dl.platformio.org/packages/manifest.json in the
``packageRepositories`` list. Platform definitions can also use custom
packages.

.. _platform_creating_manifest_file:

Manifest File ``platform.json``
-------------------------------

Each platform definition includes a *manifest file* with a particular
format that is parsed by PlatformIO when handling projects using that
platform.

Here is an example ``platform.json`` for the fictitious platform "myplatform":

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

Each platform definition must include a ``main.py``.

PlatformIO's build script is based on a next-generation build tool
named `SCons <http://www.scons.org>`_. PlatformIO has its own built-in
firmware builder ``env.BuildProgram`` with deep library search. Please
see the following template as start for developing your own ``main.py``.

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

        UPLOADER=join("$PIOPACKAGES_DIR", "tool-bar", "uploader"),
        UPLOADCMD="$UPLOADER $SOURCES"
    )

    env.Append(
        ARFLAGS=["..."],

        ASFLAGS=["flag1", "flag2", "flagN"],
        CCFLAGS=["flag1", "flag2", "flagN"],
        CXXFLAGS=["flag1", "flag2", "flagN"],
        LINKFLAGS=["flag1", "flag2", "flagN"],

        CPPDEFINES=["DEFINE_1", "DEFINE=2", "DEFINE_N"],

        LIBS=["additional", "libs", "here"],

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

Using the "myplatform" platform example above:

1. Create a ``platforms`` directory in :ref:`projectconf_pio_core_dir` if it
   doesn't exist.
2. Create a ``myplatform`` directory in ``platforms``
3. Copy the ``platform.json`` and ``builder/main.py`` files to the ``myplatform`` directory.
4. Search the available platforms via the :ref:`cmd_platform_search` command. You
   should see the new ``myplatform`` platform.
5. Install the ``myplatform`` platform via the :ref:`cmd_platform_install` command.

Now, you can use ``myplatform`` as value for the :ref:`projectconf_env_platform`
option in :ref:`projectconf`.

Examples
--------

Please take a look at the source code of existing
`PlatformIO Development Platforms <https://github.com/topics/platformio-platform>`_.

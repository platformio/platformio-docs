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

Examples
--------

Please take a look at the source code of existing
`PlatformIO Development Platforms <https://github.com/topics/platformio-platform>`_.

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
manifest. Custom packages can be uploaded to the PlatformIO Registry using :ref:`cmd_package_publish` command.

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
      "homepage": "https://mycompany.com",
      "license": "Apache-2.0",
      "keywords": ["keyword_1", "keyword_N"],
      "repository": {
        "type": "git",
        "url": "https://github.com/platformio/platform-myplatform.git"
      },
      "version": "0.0.0",
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
          "owner": "platformio",
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
      },
      "pythonPackages": {
        "pypi-pkg-1": "1.2.3",
        "pypi-pkg-2": ">=2.3, <3"
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

Publishing
----------

You can publish a development platform to the **PlatformIO Trusted Registry**
using :ref:`cmd_package_publish` command. Other developers will be able to install it.
Every time when you modify a source code of a development platform you will need to
increment the "version" field in "platform.json" manifest and re-publish again.

If the published development platform has an issue and you would like to remove it from
the PlatformIO Trusted Registry, please use :ref:`cmd_package_unpublish` command.

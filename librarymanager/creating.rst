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

.. _library_creating:

Creating Library
================

Managing components between the projects is a historical issue. A common code
is duplicated between different projects that lead to project complexity.
A good practice is to organize interdependent components as the separate libraries
where other projects can depend on them.

PlatformIO has a built-in :ref:`librarymanager` where developers can declare project
dependencies and PlatformIO will automatically manage them (install, build, update).
It doesn't have any requirements for a library source code structure.
The only requirement is a library manifest file -
:ref:`library_json`, `library.properties <https://github.com/arduino/Arduino/wiki/Arduino-IDE-1.5:-Library-specification#library-metadata>`_, or `module.json <http://docs.yottabuild.org/reference/module.html>`_.
It must be located in the root of a library.

We highly recommend using :ref:`library_json` for better compatibility and avoiding any issues.

.. contents:: Contents
    :local:

Structure
---------

We recommend to use ``src`` folder for your C/C++ source files and ``include`` folder
for your headers. You can also have nested sub-folders in ``src`` or ``include``.

**Example**

.. code::

    ├── examples
    │   └── echo
    ├── include
    │   └── HelloWorld.h
    ├── library.json
    └── src
        └── HelloWorld.cpp

Manifest
--------

A library package must contain a manifest. We recommend using :ref:`library_json`.

**Example**

.. code-block:: javascript

    {
      "name": "HelloWorld",
      "version": "1.0.0",
      "description": "A \"Hello world\" program is a computer program that outputs \"Hello World\" (or some variant) on a display device",
      "keywords": "planet, happiness, people",
      "repository":
      {
        "type": "git",
        "url": "https://github.com/username/hello-world.git"
      },
      "authors":
      [
        {
          "name": "John Smith",
          "email": "me@john-smith.com",
          "url": "https://www.john-smith/contact"
        },
        {
          "name": "Andrew Smith",
          "email": "me@andrew-smith.com",
          "url": "https://www.andrew-smith/contact",
          "maintainer": true
        }
      ],
      "license": "MIT",
      "homepage": "https://www.helloworld.org/",
      "dependencies": {
        "ownername/print": "~1.3.0"
      },
      "frameworks": "*",
      "platforms": "*"
    }


Publishing
----------

You can publish a library to the `PlatformIO Registry <https://platformio.org/lib>`__
using :ref:`cmd_package_publish` command. Every time when you modify a source code of
a library you will need to increment the "version" field in :ref:`library_json` manifest
and re-publish again.

If the published library has an issue and you would like to remove it from the PlatformIO
Registry, please use :ref:`cmd_package_unpublish` command.

Examples
--------

See the published libraries in `PlatformIO Registry <https://platformio.org/lib>`__.

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

Project Structure
-----------------

.. contents::
   :local:

Best Practices
~~~~~~~~~~~~~~

Unit tests are as important to a firmware/program ("application") as the production
source code. As with the regular code, you need to give careful thought to where
the tests reside, both physically and logically, in relation to the code under test.
If you put unit tests in the wrong place, the tests you have written may not be run.

Similarly, if you do not devise ways to reuse parts of your tests and use
test hierarchy, you will end up with test code that is either unmaintainable
or hard to understand. So, what makes a good test?

1. **Tests should be independent and repeatable.**
   It is a pain to debug a test that succeeds or fails as a result of other tests.
   PlatformIO isolates the tests by running each of them as a separate application.
   When a test fails, PlatformIO allows you to run it in isolation for quick debugging.

2. **Tests should not depend on the main application source code.**
   In PlatformIO, each test is an independent application and should contain its
   own ``main()`` function (``setup() / loop()`` for :ref:`framework_arduino`,
   ``app_main()`` for :ref:`framework_espidf`).
   Linking the main application source code from :ref:`projectconf_pio_src_dir`
   with a test suite code will lead to multiple compilation errors.
   Hence, the :ref:`unit_testing_shared_code` is disabled by default.

3. **Tests should be well organized and reflect the structure of the tested code.**
   PlatformIO lets you organize tests using nested folders. The only folder with
   a name prefixed by ``test_`` is nominated for unit testing and is an independent
   test/application. See :ref:`unit_testing_test_hierarchy`.

.. _unit_testing_shared_code:

Shared Code
~~~~~~~~~~~

By default, PlatformIO does not build the main source code from the :ref:`projectconf_pio_src_dir`
folder in pair with a test source code. If you have a shared/common code
between your "main" and "test" programs, you have 2 options:

1. We recommend splitting the source code into multiple
   components and placing them into the :ref:`projectconf_pio_lib_dir` (project's
   private libraries and components). :ref:`ldf` will find and include these libraries
   automatically in the build process. You can include any library/component header file
   in your test or main application source code using ``#include <MyComponent.h>``.

   See `Local & Embedded: Calculator <https://github.com/platformio/platformio-examples/tree/develop/unit-testing/calculator>`__
   for an example, where we have a "calculator" component in the
   :ref:`projectconf_pio_lib_dir` folder and include it in the tests and
   the main application using ``#include <calculator.h>``.

2. **NOT RECOMMENDED**. Manually instruct PlatformIO to build the main source code
   from the :ref:`projectconf_pio_src_dir` folder in pair with a test source code using
   the :ref:`projectconf_test_build_src` option in :ref:`projectconf`:

   .. code-block:: ini

      [env:myenv]
      platform = ...
      test_build_src = true

   This is very useful if you unit test independent libraries where you
   can't split source code.

   .. warning::
       Please note that you will need to use ``#ifdef PIO_UNIT_TESTING`` and ``#endif``
       guard to hide non-test related source code. For example, own ``main()``,
       ``setup() / loop()``, or ``app_main()`` functions.

.. _unit_testing_test_hierarchy:

Test Hierarchy
~~~~~~~~~~~~~~

.. versionadded:: 6.0

PlatformIO looks for the tests in the project :ref:`projectconf_pio_test_dir`.
The only folder with a name prefixed by ``test_`` is nominated for unit testing
and should be an independent test/application with its own ``main()`` function
(``setup() / loop()`` for :ref:`framework_arduino`, ``app_main()``
for :ref:`framework_espidf`). Nested folders are supported and will help you
to organize your tests.

The root :ref:`projectconf_pio_test_dir` and a folder of the active test are
automatically added to the ``CPPPATH`` scope (C Preprocessor Search Path).
Also, C/C++ files located in the root of :ref:`projectconf_pio_test_dir` will
be compiled together with the active test source files. The root
:ref:`projectconf_pio_test_dir` is useful for placing configuration
and extra C/C++ files related to the :ref:`unit_testing_frameworks`.

**Example of Pizza Project**

Let's demystify how PlatformIO handles unit tests using a virtual "Pizza Project"
having the following structure:

.. code::

   project_dir
   ├── include
   │   └── pizza_config.h
   ├── lib
   │   ├── Cheese
   │   │   ├── include
   │   │   │   └── cheese.h
   │   │   └── src
   │   │       └── cheese.cpp
   │   ├── Dough
   │   │   ├── include
   │   │   │   └── dough.h
   │   │   └── src
   │   │       └── dough.cpp
   │   └── Sauce
   │       ├── include
   │       │   └── sauce.h
   │       └── src
   │           └── sauce.cpp
   ├── platformio.ini
   ├── src
   │   └── baking.cpp
   └── test
      ├── embedded
      │   ├── components
      │   │   └── sauce
      │   │       └── test_tomatos
      │   │           └── prepare.cpp
      │   ├── stove
      │   │   ├── test_humidity
      │   │   │   ├── measure.cpp
      │   │   │   └── sensor.cpp
      │   │   └── test_temperature
      │   │       ├── measure.cpp
      │   │       └── sensor
      │   │           ├── sensor.cpp
      │   │           └── sensor.h
      │   ├── unity_config.cpp
      │   └── unity_config.h
      └── test_ingredients
         ├── include
         │   ├── cheese.h
         │   ├── vegetables.h
         │   ├── water.h
         │   ├── wheat.h
         │   └── yeast.h
         └── weighing.cpp

The main source code ("pizza baking") is located in the ``src`` folder.
This is a production code. A cooking process consists of multiple subprocesses
and depends on the components located in the ``lib`` folder. Each pizza's component
can be tested independently using unit testing.

The Pizza Project consists of 4 independent tests:

#. ``embedded/components/sauce/test_tomatos``
#. ``embedded/stove/test_humidity``
#. ``embedded/stove/test_temperature``
#. ``test_ingredients``

PlatformIO treats each test as an independent micro project with its own source
files and subfolders. You can include local header files using the relative paths.
For example, the ``test_ingredients/weighing.cpp`` source file includes
``cheese.h`` as ``#include <include/cheese.h>``.

The ``unity_config.h`` and ``unity_config.cpp`` files are located in the
``embedded`` folder and are common for the ``embedded/components/sauce/test_tomatos``,
``embedded/stove/test_humidity``, and ``embedded/stove/test_temperature`` tests.
This allows you to run a group of tests only on the embedded target and route
a test result output to the custom Serial/UART interface.
On the other hand, the ``test_ingredients`` test uses the default Unity configuration
provided by PlatformIO. For more details, please check the documentation for the
:ref:`unit_testing_frameworks_unity` testing framework.

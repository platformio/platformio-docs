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

.. _unit_testing_test_hierarchy:

Test Hierarchy
--------------

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

-----

*  If you have a single test application, you can place the source code files
   directly in the :ref:`projectconf_pio_test_dir` folder
*  If you want several test applications, you can organize them in subfolders
   under :ref:`projectconf_pio_test_dir`:

   -  each test application goes into a subfolder with a name **starting**
      with ``test_``
   -  additional levels of folders are allowed to properly organize your
      tests - see the example **Pizza Project** below
   -  the :ref:`projectconf_test_filter` option in :ref:`projectconf` or
      the :option:`pio test --filter` option on the CLI will restrict
      the tests to only those test suites whose path is relative to the
      :ref:`projectconf_pio_test_dir` and matches the filter
   -  the :ref:`projectconf_test_ignore` option in :ref:`projectconf`
      or the :option:`pio test --ignore` option on the CLI will ignore
      test suites whose path is relative to the
      :ref:`projectconf_pio_test_dir` and matches the filter.

Example of using the filter / ignore option in :ref:`projectconf` for
the **Pizza Project** below:

.. code:: ini

   [env:myenv]
   test_filter = embedded/*
   test_ignore = embedded/components/*

will only execute the ``embedded/stove/test_humidity``,
``embedded/stove/test_temperature`` test suites and will
ignore the ``embedded/components/sauce/test_tomatos`` test suite.

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

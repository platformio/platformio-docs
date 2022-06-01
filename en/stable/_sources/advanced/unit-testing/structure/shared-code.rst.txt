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

.. _unit_testing_shared_code:

Shared Code
-----------

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
       Please note that you will need to use ``#ifndef PIO_UNIT_TESTING`` and ``#endif``
       guard to hide non-test related source code. For example, own ``main()``,
       ``setup() / loop()``, or ``app_main()`` functions.

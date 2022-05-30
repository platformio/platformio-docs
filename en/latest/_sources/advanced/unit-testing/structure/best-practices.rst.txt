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

Best Practices
--------------

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
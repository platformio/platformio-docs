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

Launch Types
------------

There are two execution orders for extra scripts:

1. **PRE** - executes before the main script of :ref:`platforms`
2. **POST** - executes after the main script of :ref:`platforms`

Multiple extra scripts are allowed. Please split them via  ", "
(comma + space) in the same line or use multi-line values.

For example, in :ref:`projectconf`:

.. code-block:: ini

  [env:my_env_1]
  platform = ...
  ; Defaults to POST script since no prefix is used
  extra_scripts = post_extra_script.py

  [env:my_env_2]
  platform = ...
  extra_scripts =
    pre:pre_extra_script.py
    post:post_extra_script1.py
    post_extra_script2.py

This option can also be set by the global environment variable :envvar:`PLATFORMIO_EXTRA_SCRIPTS`.

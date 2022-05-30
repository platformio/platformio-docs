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

``name``
--------

**Required** | Type: ``String`` | Max. Length: 50

A name of a library.

* Must be unique in the `PlatformIO Registry <https://registry.platformio.org>`__
* Should be slug style for simplicity, consistency, and compatibility.
  Example: *HelloWorld*
* Can contain a-z, digits, and dashes (but not start/end with them)
* Consecutive dashes and [:;/,@<>] chars are not allowed.
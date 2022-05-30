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

.. _manifest_library_json_repository:

``repository``
--------------

*Optional* | Type: ``Object``

The repository in which the source code can be found. The field consists of the
next items:

* ``type`` the only "git", "hg" or "svn" are supported
* ``url``
* ``branch`` if is not specified, default branch will be used. This field will
  be ignored if tag/release exists with the value of :ref:`manifest_library_json_version`.

**Example**

.. code-block:: javascript

    "repository":
    {
        "type": "git",
        "url": "https://github.com/foo/bar.git"
    }
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

``includeDir``
~~~~~~~~~~~~~~

*Optional* | Type: ``String``

Custom directory to be searched for header files.
A default value is ``include`` and means that folder is located at
the root of a library.

.. note::
    The :ref:`ldf` will pick a library automatically only when
    a project or other dependent libraries include any header file
    located in ``includeDir`` or ``srcDir``.

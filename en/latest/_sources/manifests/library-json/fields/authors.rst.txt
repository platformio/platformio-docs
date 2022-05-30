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

.. _manifest_library_json_authors:

``authors``
-----------

*Optional* | Type: ``Object`` or ``Array``

An author contact information

* ``name`` Full name (**Required**)
* ``email``
* ``url`` An author's contact page
* ``maintainer`` Specify "maintainer" status

**Examples**

.. code-block:: javascript

    "authors":
    {
        "name": "John Smith",
        "email": "me@john-smith.com",
        "url": "https://www.john-smith/contact"
    }

    ...

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
    ]


.. note::
    If :ref:`manifest_library_json_authors` field is not defined, PlatformIO will try to fetch data
    from VCS provider (Github, Gitlab, etc) if :ref:`manifest_library_json_repository` is declared.
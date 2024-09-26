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

.. _faq_install_python:

Install Python Interpreter
--------------------------

:ref:`piocore` is written in `Python <https://www.python.org/downloads/>`_ that
is installed by default on all the popular OSs except Windows.

Please navigate to official website and `Download the latest Python <https://www.python.org/downloads/>`_
and install it. Please **READ NOTES BELOW**.

:Linux:
  Most linux distributions will include a Python installation already. You may need to ensure that the Python Virtual Environment is installed.

  Debian/Ubuntu derivatives have this package in Apt as ``python3-venv``.

  ``sudo apt install python3-venv`` should be all that is required.

  For more details, please check the `platformio-core-installer/issues/85 <https://github.com/platformio/platformio-core-installer/issues/85>`__.

:macOS:
  Please read the "Important Information" displayed during installation for information
  about SSL/TLS certificate validation and the running the **"Install Certificates.command"**.

  If you do not install SSL/TLS certificates, PlatformIO will not be able to download
  dependent packages, libraries, and toolchains.

:Windows:
  Please select ``Add Python to Path`` (see below), otherwise, ``python`` command will
  not be available.

  .. image:: ../_static/images/python-installer-add-path.png

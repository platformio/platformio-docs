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

.. _what_is_pio:

What is PlatformIO?
===================

**A place where Developers and Teams have true Freedom! No more vendor lock-in!**

.. contents:: Contents
    :local:

PlatformIO is a cross-platform, cross-architecture, multiple framework, professional
tool for embedded systems engineers and for software developers who write applications
for embedded products.

Awards
------

PlatformIO was nominated for the year's `best Software and Tools in the 2015/16 IoT Awards <http://www.postscapes.com/2015-16/best-iot-software-and-tools/>`_.

A native `PlatformIO IDE extension <https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide>`__
for Microsoft :ref:`ide_vscode` editor is the most rated/reviewed extension with over 800
five-star reviews in the whole Microsoft Marketplace. It also was installed by over
750,000 unique developers around the world.

Philosophy
----------

PlatformIO's unique philosophy in the embedded market provides developers with a modern
integrated development environment (:ref:`ide`) that works cross-platform,
supports many different software development kits (SDKs) or :ref:`frameworks`, and
includes sophisticated debugging (:ref:`piodebug`), unit testing (:ref:`unit_testing`),
automated code analysis (:ref:`piocheck`), and remote management (:ref:`pioremote`).
It is architected to maximize flexibility and choice by developers, who can use either
graphical or command line editors (:ref:`piocore`), or both.

PlatformIO is a must-have tool for professional embedded systems engineers who develop
solutions on more than one specific platform. In addition, by having a decentralized
architecture, PlatformIO offers both new and existing developers a quick integration
path for developing commercial-ready products, and reduces the overall time-to-market.

And it runs on any one of your favorite modern operating systems (macOS, MS Windows,
Linux, FreeBSD).

Technologies
------------

PlatformIO applies the latest scalable and flexible software technology to the embedded
market – an area traditionally served by complex software tools that experienced
hardware engineers have learned over time (often painfully so). Instead, with
PlatformIO, users can be hobbyists or professionals. They can import the classic
Arduino "Blink" sketch or develop  a sophisticated low-level embedded C program for a
commercial product. Example code for any supported framework can be compiled and
uploaded to a target platform in minutes.

The build system structure automatically tags software dependencies and applies them
using a modular hierarchy that takes away the usual complexity and pain. Developers no
longer have to manually find and assemble an environment of toolchains, compilers, and
library dependencies to develop applications for a specific target. With PlatformIO,
clicking the compile button will bring in all necessary dependencies automatically. It's
analogous to if you were a furniture designer, and your CAD program had a "build" button
that caused a robot to fetch all the necessary pieces and fasteners and correctly
assemble them.

:ref:`piocore` is a unique, developed-from-scratch build system that removes the usual
pain of software integration, packaging, and library dependencies that developers
encounter when they move beyond the bounds of a specific SDK or example embedded
application. It can be used with a variety of code development environments and allows
easy integration with numerous cloud platforms and web services feeds. The user
experiences no barriers to getting started quickly: **no license fees, no legal contracts**.
The user maintains full flexibility of the build environment because the tools are open
source and permissively licensed (no permission needed to modify them, and no
requirement to share changes.)

Problematic
-----------

* The main problem which repulses people from the embedded world is a complicated
  process to setup development software for a specific MCU/board: toolchains,
  proprietary vendor's IDE (which sometimes isn't free) and what is more,
  to get a computer with OS where that software is supported.
* Multiple hardware platforms (MCUs, boards) require different toolchains,
  IDEs, etc, and, respectively, spending time on learning new development environments.
* Finding proper libraries and code samples showing how to use popular
  sensors, actuators, etc.
* Sharing embedded projects between team members, regardless of an operating
  system they prefer to work with.

How does it work?
-----------------

Without going too deep into PlatformIO implementation details, work cycle of
the project developed using PlatformIO is as follows:

* Users choose board(s) interested in :ref:`projectconf`
* Based on this list of boards, PlatformIO downloads required toolchains and
  installs them automatically.
* Users develop code and PlatformIO makes sure that it is compiled, prepared
  and uploaded to all the boards of interest.

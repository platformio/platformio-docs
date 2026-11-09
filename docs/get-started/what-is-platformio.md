<a id="what-is-pio"></a>

# What is PlatformIO? {#what-is-platformio}

**A place where Developers and Teams have true Freedom! No more vendor lock-in!**

PlatformIO is a cross-platform, cross-architecture, multiple framework, professional tool for embedded systems engineers and for software developers who write applications for embedded products.

## Awards {#awards}

PlatformIO was nominated for the year's [best Software and Tools in the 2015/16 IoT Awards](http://www.postscapes.com/2015-16/best-iot-software-and-tools/).

A native [PlatformIO IDE extension](https://marketplace.visualstudio.com/items?itemName=platformio.platformio-ide) for Microsoft [PlatformIO IDE for VSCode](../guides/ide/vscode.md) editor is the most rated/reviewed extension with over 2,500 five-star reviews in the whole Microsoft Marketplace. It also was installed by over 3,000,000 unique developers around the world.

## Philosophy {#philosophy}

PlatformIO's unique philosophy in the embedded market provides developers with a modern integrated development environment ([Cloud & Desktop IDEs](../guides/ide/index.md)) that works cross-platform, supports many different software development kits (SDKs) or [Frameworks](../hardware/frameworks/index.md), and includes sophisticated debugging ([Debugging](../guides/debugging/index.md)), unit testing ([Unit Testing](../guides/unit-testing/index.md)), automated code analysis ([Static Code Analysis](../guides/static-code-analysis/index.md)), and remote management ([Remote Development](../guides/remote-development.md)). It is architected to maximize flexibility and choice by developers, who can use either graphical or command line editors ([PlatformIO Core (CLI)](./platformio-core.md)), or both.

PlatformIO is a must-have tool for professional embedded systems engineers who develop solutions on more than one specific platform. In addition, by having a decentralized architecture, PlatformIO offers both new and existing developers a quick integration path for developing commercial-ready products, and reduces the overall time-to-market.

And it runs on any one of your favorite modern operating systems (macOS, MS Windows, Linux, FreeBSD).

## Technologies {#technologies}

PlatformIO applies the latest scalable and flexible software technology to the embedded market – an area traditionally served by complex software tools that experienced hardware engineers have learned over time (often painfully so). Instead, with PlatformIO, users can be hobbyists or professionals. They can import the classic Arduino "Blink" sketch or develop  a sophisticated low-level embedded C program for a commercial product. Example code for any supported framework can be compiled and uploaded to a target platform in minutes.

The build system structure automatically tags software dependencies and applies them using a modular hierarchy that takes away the usual complexity and pain. Developers no longer have to manually find and assemble an environment of toolchains, compilers, and library dependencies to develop applications for a specific target. With PlatformIO, clicking the compile button will bring in all necessary dependencies automatically. It's analogous to if you were a furniture designer, and your CAD program had a "build" button that caused a robot to fetch all the necessary pieces and fasteners and correctly assemble them.

[PlatformIO Core (CLI)](./platformio-core.md) is a unique, developed-from-scratch build system that removes the usual pain of software integration, packaging, and library dependencies that developers encounter when they move beyond the bounds of a specific SDK or example embedded application. It can be used with a variety of code development environments and allows easy integration with numerous cloud platforms and web services feeds. The user experiences no barriers to getting started quickly: **no license fees, no legal contracts**. The user maintains full flexibility of the build environment because the tools are open source and permissively licensed (no permission needed to modify them, and no requirement to share changes.)

## Problematic {#problematic}

- The main problem which repulses people from the embedded world is a complicated process to setup development software for a specific MCU/board: toolchains, proprietary vendor's IDE (which sometimes isn't free) and what is more, to get a computer with OS where that software is supported.
- Multiple hardware platforms (MCUs, boards) require different toolchains, IDEs, etc, and, respectively, spending time on learning new development environments.
- Finding proper libraries and code samples showing how to use popular sensors, actuators, etc.
- Sharing embedded projects between team members, regardless of an operating system they prefer to work with.

## How does it work? {#how-does-it-work}

Without going too deep into PlatformIO implementation details, work cycle of the project developed using PlatformIO is as follows:

- Users choose board(s) interested in ["platformio.ini" (Project Configuration File)](../reference/platformio-ini/index.md)
- Based on this list of boards, PlatformIO downloads required toolchains and installs them automatically.
- Users develop code and PlatformIO makes sure that it is compiled, prepared and uploaded to all the boards of interest.

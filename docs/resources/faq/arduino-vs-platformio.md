---
description: How Arduino IDE and PlatformIO IDE differ, and when to use which.
---

# Arduino IDE or PlatformIO IDE?

Both can build and upload code for Arduino boards. Which one fits depends on
your project.

| | Arduino IDE | [PlatformIO IDE](../../get-started/platformio-ide.md) |
| --- | --- | --- |
| Best for | Getting started, small sketches | Larger projects, teams, professional work |
| Hardware | Boards with an Arduino core | 1,500+ boards across 30+ platforms, with the [Arduino](/hardware/frameworks/arduino) framework or vendor SDKs and RTOSes |
| Libraries | Installed globally | [Declared per project](../../guides/libraries/dependencies.md), with pinned versions |
| Debugging | Limited | [Full debugger](../../guides/debugging/index.md) with breakpoints and registers |
| Testing and CI | Not built in | [Unit testing](../../guides/unit-testing/index.md), [static analysis](../../guides/static-code-analysis/index.md), [CI](../../guides/ci/index.md) |

You can move an Arduino sketch to PlatformIO at any time: create a project
for your board with the Arduino framework and copy the sketch into `src`.

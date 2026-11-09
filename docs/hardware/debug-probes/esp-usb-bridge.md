<a id="debugging-tool-esp-usb-bridge"></a>

# ESP USB Bridge {#esp-usb-bridge}

[![](./img/esp-usb-bridge.png)](https://github.com/espressif/esp-usb-bridge?utm_source=platformio&utm_medium=docs)

The ESP USB Bridge is an ESP-IDF project utilizing an ESP32-S2 (or optionally, an ESP32-S3) chip to create a bridge between a computer (PC) and a target microcontroller (MCU). It can serve as a replacement for USB-to-UART chips (e.g. CP210x). Official reference can be found [here](https://github.com/espressif/esp-usb-bridge?utm_source=platformio&utm_medium=docs).

## Configuration {#configuration}

You can configure debugging tool using [debug_tool](../../reference/platformio-ini/env/debug-tool.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md):

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = esp-usb-bridge
```

If you would like to use this tool for firmware uploading, please change upload protocol:

```ini
[env:myenv]
platform = ...
board = ...
debug_tool = esp-usb-bridge
upload_protocol = esp-usb-bridge
```

More options:

- [Debugging options](../../reference/platformio-ini/env/debug-options.md)
- [Upload options](../../reference/platformio-ini/env/upload-options.md)

## Tutorials {#tutorials}

- [Use the PlatformIO Debugger on the ESP32 Using an ESP-prog](https://www.hackster.io/brian-lough/use-the-platformio-debugger-on-the-esp32-using-an-esp-prog-f633b6)

<!-- begin_platforms -->

## Platforms {#platforms}

| Name | Description |
|---|---|
| [Espressif 32](/hardware/platforms/espressif32) | Espressif Systems is a privately held fabless semiconductor company. They provide wireless communications and Wi-Fi chips which are widely used in mobile devices and the Internet of Things applications. |

## Frameworks {#frameworks}

| Name | Description |
|---|---|
| [Arduino](/hardware/frameworks/arduino) | Arduino Wiring-based Framework allows writing cross-platform software to control devices attached to a wide range of Arduino boards to create all kinds of creative coding, interactive objects, spaces or physical experiences |
| [Espressif IoT Development Framework](/hardware/frameworks/espidf) | ESP-IDF is the official development framework for the ESP32 and ESP32-S Series SoCs. |

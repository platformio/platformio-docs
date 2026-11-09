---
sidebar_label: "Linux udev rules"
description: Give your Linux user access to boards and debug probes with the PlatformIO udev rules.
---

# Install the udev rules (Linux) {#platformio-udev-rules}

On Linux, a regular user cannot access most USB serial devices and debug
probes. The PlatformIO [udev](https://en.wikipedia.org/wiki/Udev) rules file,
`99-platformio-udev.rules`, grants access to the boards and probes that
PlatformIO supports, so that you can upload and debug without `sudo`.

## Install the rules {#install-the-rules}

1. Download the latest rules into `/etc/udev/rules.d/`:

   ```bash
   curl -fsSL https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules | sudo tee /etc/udev/rules.d/99-platformio-udev.rules
   ```

   If you downloaded the
   [file](https://raw.githubusercontent.com/platformio/platformio-core/develop/platformio/assets/system/99-platformio-udev.rules)
   yourself, copy it instead:

   ```bash
   sudo cp 99-platformio-udev.rules /etc/udev/rules.d/99-platformio-udev.rules
   ```

   On some distributions the file must be in `/lib/udev/rules.d/` instead.

2. Reload the rules:

   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

   On older systems, `sudo service udev restart` does the same.

3. Unplug the board and plug it in again.

:::note

If your board still is not accessible, check that its USB vendor and product
IDs (VID and PID) are in the rules file. To see them, run
[`pio device list`](../../reference/cli/pio-device/list.md).

:::

## Alternative: join the device group {#alternative-using-group-membership}

Instead of installing the rules, you can add your user to the group that owns
the serial device. This works for serial ports, but not for every debug probe.

1. Connect the board and find its port with
   [`pio device list`](../../reference/cli/pio-device/list.md), for example
   `/dev/ttyACM0`.
2. Find the group that owns the port:

   ```bash
   ls -l /dev/ttyACM0
   ```

   ```text
   crw-rw---- 1 root dialout 166, 0 Jul 10 13:43 /dev/ttyACM0
   ```

   Here the group is `dialout`. Typical names are `dialout`, `plugdev`
   (Debian, Ubuntu, Fedora) and `uucp` (Arch Linux).

3. Add your user to that group:

   ```bash
   sudo usermod -a -G dialout $USER
   ```

4. Sign out and sign back in (or restart). Run `id` to check that the group is
   listed.

:::note

`sudo chmod a+rw /dev/ttyACM0` also grants access, but only until the device
is disconnected.

:::

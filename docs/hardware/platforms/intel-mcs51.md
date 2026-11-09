---
title: "Intel MCS-51 (8051)"
custom_edit_url: "https://github.com/platformio/platformio-core/blob/develop/scripts/docspregen.py"
---

<a id="platform-intel-mcs51"></a>

# Intel MCS-51 (8051)

**Registry:** [https://registry.platformio.org/platforms/platformio/intel_mcs51](https://registry.platformio.org/platforms/platformio/intel_mcs51)  
**Configuration:** [platform](../../reference/platformio-ini/env/platform.md) = `platformio/intel_mcs51`

The Intel MCS-51 (commonly termed 8051) is an internally Harvard architecture, complex instruction set computer (CISC) instruction set, single chip microcontroller (uC) series developed by Intel in 1980 for use in embedded systems.

For more detailed information please visit [vendor site](https://en.wikipedia.org/wiki/Intel_MCS-51?utm_source=platformio.org&utm_medium=docs).

## Examples

Examples are listed from [Intel MCS-51 (8051) development platform repository](https://github.com/platformio/platform-intel_mcs51/tree/master/examples?utm_source=platformio.org&utm_medium=docs):

- [anymcu-blink](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/anymcu-blink?utm_source=platformio.org&utm_medium=docs)
- [stc-header](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-header?utm_source=platformio.org&utm_medium=docs)
- [assembly-blink](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/assembly-blink?utm_source=platformio.org&utm_medium=docs)
- [native-blink](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/native-blink?utm_source=platformio.org&utm_medium=docs)
- [anymcu-header](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/anymcu-header?utm_source=platformio.org&utm_medium=docs)
- [stc-blink](https://github.com/platformio/platform-intel_mcs51/tree/master/examples/stc-blink?utm_source=platformio.org&utm_medium=docs)

## Stable and upstream versions

You can switch between [stable releases](https://github.com/platformio/platform-intel_mcs51/releases) of Intel MCS-51 (8051) development platform and the latest upstream version using [platform](../../reference/platformio-ini/env/platform.md) option in ["platformio.ini" (Project Configuration File)](../../reference/platformio-ini/index.md) as described below.

### Stable

```ini
; Latest stable version, NOT recommended
; Pin the version as shown below
[env:latest_stable]
platform = intel_mcs51
board = ...

; Specific version
[env:custom_stable]
platform = intel_mcs51@x.y.z
board = ...
```

### Upstream

```ini
[env:upstream_develop]
platform = https://github.com/platformio/platform-intel_mcs51.git
board = ...
```

## Packages

| Name | Description |
|---|---|
| [tool-stcgal](https://registry.platformio.org/tools/platformio/tool-stcgal) | Open Source STC MCU ISP flash tool |
| [tool-vnproch55x](https://registry.platformio.org/tools/platformio/tool-vnproch55x) | CH55X Programming software |
| [toolchain-sdcc](https://registry.platformio.org/tools/platformio/toolchain-sdcc) | Small Device C compiler suite |

:::warning

**Linux Users**:

- Install "udev" rules [99-platformio-udev.rules](../../get-started/install/udev-rules.md)
- Raspberry Pi users, please read this article [Enable serial port on Raspberry Pi](https://hallard.me/enable-serial-port-on-raspberry-pi/).

**Windows Users:**

Please check that you have a correctly installed USB driver from board manufacturer

:::

## Boards

:::note

- You can list pre-configured boards by [pio boards](../../reference/cli/pio-boards.md) command
- For more detailed `board` information please scroll the tables below by horizontally.

:::

### Intel & Licensees

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Generic 8051](../boards/intel-mcs51/generic8051.md) | No | 8051 | 11MHz | 4KB | 128B |

### Intel & licensees

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Generic 8052](../boards/intel-mcs51/generic8052.md) | No | 8052 | 11MHz | 8KB | 256B |

### Microchip & Atmel

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Generic AT89S51](../boards/intel-mcs51/at89s51.md) | No | AT89S51 | 11MHz | 4KB | 128B |
| [Generic AT89S52](../boards/intel-mcs51/at89s52.md) | No | AT89S52 | 11MHz | 8KB | 256B |

### Nuvoton

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Generic ML51BB9AE](../boards/intel-mcs51/ml51bb9ae.md) | No | ML51BB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51DB9AE](../boards/intel-mcs51/ml51db9ae.md) | No | ML51DB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51EB9AE](../boards/intel-mcs51/ml51eb9ae.md) | No | ML51EB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51EC0AE](../boards/intel-mcs51/ml51ec0ae.md) | No | ML51EC0AE | 24MHz | 32KB | 2.25KB |
| [Generic ML51FB9AE](../boards/intel-mcs51/ml51fb9ae.md) | No | ML51FB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51LD1AE](../boards/intel-mcs51/ml51ld1ae.md) | No | ML51LD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML51OB9AE](../boards/intel-mcs51/ml51ob9ae.md) | No | ML51OB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51PB9AE](../boards/intel-mcs51/ml51pb9ae.md) | No | ML51PB9AE | 24MHz | 16KB | 2.25KB |
| [Generic ML51PC0AE](../boards/intel-mcs51/ml51pc0ae.md) | No | ML51PC0AE | 24MHz | 32KB | 2.25KB |
| [Generic ML51SD1AE](../boards/intel-mcs51/ml51sd1ae.md) | No | ML51SD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML51TB9AE](../boards/intel-mcs51/ml51tb9ae.md) | No | ML51TB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML51TC0AE](../boards/intel-mcs51/ml51tc0ae.md) | No | ML51TC0AE | 24MHz | 32KB | 2.25KB |
| [Generic ML51TC1AE](../boards/intel-mcs51/ml51tc1ae.md) | No | ML51TC1AE | 24MHz | 32KB | 2.25KB |
| [Generic ML51TD1AE](../boards/intel-mcs51/ml51td1ae.md) | No | ML51TD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML51UB9AE](../boards/intel-mcs51/ml51ub9ae.md) | No | ML51UB9AE | 24MHz | 16KB | 2.25KB |
| [Generic ML51UC0AE](../boards/intel-mcs51/ml51uc0ae.md) | No | ML51UC0AE | 24MHz | 32KB | 2.25KB |
| [Generic ML51XB9AE](../boards/intel-mcs51/ml51xb9ae.md) | No | ML51XB9AE | 24MHz | 16KB | 1.25KB |
| [Generic ML54LD1AE](../boards/intel-mcs51/ml54ld1ae.md) | No | ML54LD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML54MD1AE](../boards/intel-mcs51/ml54md1ae.md) | No | ML54MD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML54SD1AE](../boards/intel-mcs51/ml54sd1ae.md) | No | ML54SD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML56LD1AE](../boards/intel-mcs51/ml56ld1ae.md) | No | ML56LD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML56MD1AE](../boards/intel-mcs51/ml56md1ae.md) | No | ML56MD1AE | 24MHz | 64KB | 4.25KB |
| [Generic ML56SD1AE](../boards/intel-mcs51/ml56sd1ae.md) | No | ML56SD1AE | 24MHz | 64KB | 4.25KB |
| [Generic MS51BA9AE](../boards/intel-mcs51/ms51ba9ae.md) | No | MS51BA9AE | 16MHz | 8KB | 1.25KB |
| [Generic MS51DA9AE](../boards/intel-mcs51/ms51da9ae.md) | No | MS51DA9AE | 16MHz | 8KB | 1.25KB |
| [Generic MS51EC0AE](../boards/intel-mcs51/ms51ec0ae.md) | No | MS51EC0AE | 16MHz | 32KB | 2.25KB |
| [Generic MS51FB9AE](../boards/intel-mcs51/ms51fb9ae.md) | No | MS51FB9AE | 16MHz | 16KB | 1.25KB |
| [Generic MS51FC0AE](../boards/intel-mcs51/ms51fc0ae.md) | No | MS51FC0AE | 16MHz | 32KB | 2.25KB |
| [Generic MS51IA9AE](../boards/intel-mcs51/ms51ia9ae.md) | No | MS51IA9AE | 16MHz | 8KB | 1.25KB |
| [Generic MS51PC0AE](../boards/intel-mcs51/ms51pc0ae.md) | No | MS51PC0AE | 16MHz | 32KB | 2.25KB |
| [Generic MS51TC0AE](../boards/intel-mcs51/ms51tc0ae.md) | No | MS51TC0AE | 16MHz | 32KB | 2.25KB |
| [Generic MS51XB9AE](../boards/intel-mcs51/ms51xb9ae.md) | No | MS51XB9AE | 16MHz | 16KB | 1.25KB |
| [Generic MS51XB9BE](../boards/intel-mcs51/ms51xb9be.md) | No | MS51XB9BE | 16MHz | 16KB | 1.25KB |
| [Generic MS51XC0BE](../boards/intel-mcs51/ms51xc0be.md) | No | MS51XC0BE | 16MHz | 32KB | 2.25KB |
| [Generic N76E003](../boards/intel-mcs51/n76e003.md) | No | N76E003 | 16MHz | 18KB | 1KB |
| [Generic N76E616](../boards/intel-mcs51/n76e616.md) | No | N76E616 | 11MHz | 18KB | 512B |
| [Generic N76E885](../boards/intel-mcs51/n76e885.md) | No | N76E885 | 22MHz | 18KB | 512B |
| [Generic N78E055](../boards/intel-mcs51/n78e055.md) | No | N78E055 | 22MHz | 16KB | 1.25KB |
| [Generic N78E059](../boards/intel-mcs51/n78e059.md) | No | N78E059 | 22MHz | 32KB | 1.25KB |
| [Generic N78E366](../boards/intel-mcs51/n78e366.md) | No | N78E366 | 22MHz | 64KB | 1.25KB |
| [Generic N78E517](../boards/intel-mcs51/n78e517.md) | No | N78E517 | 22MHz | 64KB | 1.25KB |
| [Generic N79E352](../boards/intel-mcs51/n79e352.md) | No | N79E352 | 22MHz | 8KB | 256B |
| [Generic N79E715](../boards/intel-mcs51/n79e715.md) | No | N79E715 | 22MHz | 16KB | 512B |
| [Generic N79E813](../boards/intel-mcs51/n79e813.md) | No | N79E813 | 22MHz | 4KB | 512B |
| [Generic N79E8132](../boards/intel-mcs51/n79e8132.md) | No | N79E8132 | 22MHz | 4KB | 512B |
| [Generic N79E814](../boards/intel-mcs51/n79e814.md) | No | N79E814 | 22MHz | 8KB | 512B |
| [Generic N79E815](../boards/intel-mcs51/n79e815.md) | No | N79E815 | 22MHz | 16KB | 512B |
| [Generic N79E822](../boards/intel-mcs51/n79e822.md) | No | N79E822 | 6MHz | 2KB | 256B |
| [Generic N79E823](../boards/intel-mcs51/n79e823.md) | No | N79E823 | 6MHz | 4KB | 256B |
| [Generic N79E824](../boards/intel-mcs51/n79e824.md) | No | N79E824 | 6MHz | 8KB | 256B |
| [Generic N79E825](../boards/intel-mcs51/n79e825.md) | No | N79E825 | 6MHz | 16KB | 256B |
| [Generic N79E843](../boards/intel-mcs51/n79e843.md) | No | N79E843 | 22MHz | 4KB | 512B |
| [Generic N79E8432](../boards/intel-mcs51/n79e8432.md) | No | N79E8432 | 22MHz | 4KB | 512B |
| [Generic N79E844](../boards/intel-mcs51/n79e844.md) | No | N79E844 | 22MHz | 8KB | 512B |
| [Generic N79E845](../boards/intel-mcs51/n79e845.md) | No | N79E845 | 22MHz | 16KB | 512B |
| [Generic N79E854](../boards/intel-mcs51/n79e854.md) | No | N79E854 | 22MHz | 8KB | 512B |
| [Generic N79E855](../boards/intel-mcs51/n79e855.md) | No | N79E855 | 22MHz | 16KB | 512B |
| [Generic N79E875](../boards/intel-mcs51/n79e875.md) | No | N79E875 | 22MHz | 16KB | 512B |
| [Generic W79E2051](../boards/intel-mcs51/w79e2051.md) | No | W79E2051 | 22MHz | 2KB | 256B |
| [Generic W79E4051](../boards/intel-mcs51/w79e4051.md) | No | W79E4051 | 22MHz | 4KB | 256B |
| [Generic W79E632](../boards/intel-mcs51/w79e632.md) | No | W79E632 | 11MHz | 64KB | 1.25KB |
| [Generic W79E633](../boards/intel-mcs51/w79e633.md) | No | W79E633 | 22MHz | 64KB | 1.25KB |
| [Generic W79E658](../boards/intel-mcs51/w79e658.md) | No | W79E658 | 22MHz | 64KB | 1.25KB |
| [Generic W79E659](../boards/intel-mcs51/w79e659.md) | No | W79E659 | 22MHz | 32KB | 1.25KB |
| [Generic W79E8213](../boards/intel-mcs51/w79e8213.md) | No | W79E8213 | 20MHz | 4KB | 128B |

### STC

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [Generic IAP12C5A62S2](../boards/intel-mcs51/iap12c5a62s2.md) | No | IAP12C5A62S2 | 11MHz | 62KB | 1.25KB |
| [Generic IAP15F106](../boards/intel-mcs51/iap15f106.md) | No | IAP15F106 | 11MHz | 6KB | 128B |
| [Generic IAP15F206A](../boards/intel-mcs51/iap15f206a.md) | No | IAP15F206A | 11MHz | 6KB | 256B |
| [Generic IAP15F2K61S](../boards/intel-mcs51/iap15f2k61s.md) | No | IAP15F2K61S | 11MHz | 61KB | 2KB |
| [Generic IAP15F2K61S2](../boards/intel-mcs51/iap15f2k61s2.md) | No | IAP15F2K61S2 | 11MHz | 61KB | 2KB |
| [Generic IAP15F413AD](../boards/intel-mcs51/iap15f413ad.md) | No | IAP15F413AD | 11MHz | 13KB | 512B |
| [Generic IAP15W105](../boards/intel-mcs51/iap15w105.md) | No | IAP15W105 | 11MHz | 5KB | 128B |
| [Generic IAP15W1K29S](../boards/intel-mcs51/iap15w1k29s.md) | No | IAP15W1K29S | 11MHz | 29KB | 1KB |
| [Generic IAP15W205S](../boards/intel-mcs51/iap15w205s.md) | No | IAP15W205S | 11MHz | 5KB | 256B |
| [Generic IAP15W413AS](../boards/intel-mcs51/iap15w413as.md) | No | IAP15W413AS | 11MHz | 13KB | 512B |
| [Generic IAP15W413S](../boards/intel-mcs51/iap15w413s.md) | No | IAP15W413S | 11MHz | 13KB | 512B |
| [Generic IAP15W4K58S4](../boards/intel-mcs51/iap15w4k58s4.md) | No | IAP15W4K58S4 | 11MHz | 58KB | 4KB |
| [Generic IAP15W4K61S4](../boards/intel-mcs51/iap15w4k61s4.md) | No | IAP15W4K61S4 | 11MHz | 61KB | 4KB |
| [Generic IAP15W4K63S4](../boards/intel-mcs51/iap15w4k63s4.md) | No | IAP15W4K63S4 | 11MHz | 63.50KB | 4KB |
| [Generic IRC15F107W](../boards/intel-mcs51/irc15f107w.md) | No | IRC15F107W | 11MHz | 6KB | 128B |
| [Generic IRC15F2K63S2](../boards/intel-mcs51/irc15f2k63s2.md) | No | IRC15F2K63S2 | 11MHz | 63.50KB | 2KB |
| [Generic IRC15W107](../boards/intel-mcs51/irc15w107.md) | No | IRC15W107 | 11MHz | 7KB | 128B |
| [Generic IRC15W1K31S](../boards/intel-mcs51/irc15w1k31s.md) | No | IRC15W1K31S | 11MHz | 31.50KB | 1KB |
| [Generic IRC15W207S](../boards/intel-mcs51/irc15w207s.md) | No | IRC15W207S | 11MHz | 7.50KB | 256B |
| [Generic IRC15W415AS](../boards/intel-mcs51/irc15w415as.md) | No | IRC15W415AS | 11MHz | 15.50KB | 512B |
| [Generic IRC15W415S](../boards/intel-mcs51/irc15w415s.md) | No | IRC15W415S | 11MHz | 15.50KB | 512B |
| [Generic STC12C5A08S2](../boards/intel-mcs51/stc12c5a08s2.md) | No | STC12C5A08S2 | 11MHz | 8KB | 1.25KB |
| [Generic STC12C5A16S2](../boards/intel-mcs51/stc12c5a16s2.md) | No | STC12C5A16S2 | 11MHz | 16KB | 1.25KB |
| [Generic STC12C5A32S2](../boards/intel-mcs51/stc12c5a32s2.md) | No | STC12C5A32S2 | 11MHz | 32KB | 1.25KB |
| [Generic STC12C5A40S2](../boards/intel-mcs51/stc12c5a40s2.md) | No | STC12C5A40S2 | 11MHz | 40KB | 1.25KB |
| [Generic STC12C5A48S2](../boards/intel-mcs51/stc12c5a48s2.md) | No | STC12C5A48S2 | 11MHz | 48KB | 1.25KB |
| [Generic STC12C5A52S2](../boards/intel-mcs51/stc12c5a52s2.md) | No | STC12C5A52S2 | 11MHz | 52KB | 1.25KB |
| [Generic STC12C5A56S2](../boards/intel-mcs51/stc12c5a56s2.md) | No | STC12C5A56S2 | 11MHz | 56KB | 1.25KB |
| [Generic STC12C5A60S2](../boards/intel-mcs51/stc12c5a60s2.md) | No | STC12C5A60S2 | 11MHz | 59.71KB | 1.25KB |
| [Generic STC15F100](../boards/intel-mcs51/stc15f100.md) | No | STC15F100 | 11MHz | 512B | 128B |
| [Generic STC15F100W](../boards/intel-mcs51/stc15f100w.md) | No | STC15F100W | 11MHz | 512B | 128B |
| [Generic STC15F101](../boards/intel-mcs51/stc15f101.md) | No | STC15F101 | 11MHz | 1KB | 128B |
| [Generic STC15F101E](../boards/intel-mcs51/stc15f101e.md) | No | STC15F101E | 11MHz | 1KB | 128B |
| [Generic STC15F101W](../boards/intel-mcs51/stc15f101w.md) | No | STC15F101W | 11MHz | 1KB | 128B |
| [Generic STC15F102](../boards/intel-mcs51/stc15f102.md) | No | STC15F102 | 11MHz | 2KB | 128B |
| [Generic STC15F102E](../boards/intel-mcs51/stc15f102e.md) | No | STC15F102E | 11MHz | 2KB | 128B |
| [Generic STC15F102W](../boards/intel-mcs51/stc15f102w.md) | No | STC15F102W | 11MHz | 2KB | 128B |
| [Generic STC15F103](../boards/intel-mcs51/stc15f103.md) | No | STC15F103 | 11MHz | 3KB | 128B |
| [Generic STC15F103E](../boards/intel-mcs51/stc15f103e.md) | No | STC15F103E | 11MHz | 3KB | 128B |
| [Generic STC15F103W](../boards/intel-mcs51/stc15f103w.md) | No | STC15F103W | 11MHz | 3KB | 128B |
| [Generic STC15F104](../boards/intel-mcs51/stc15f104.md) | No | STC15F104 | 11MHz | 4KB | 128B |
| [Generic STC15F104E](../boards/intel-mcs51/stc15f104e.md) | No | STC15F104E | 11MHz | 4KB | 128B |
| [Generic STC15F104W](../boards/intel-mcs51/stc15f104w.md) | No | STC15F104W | 11MHz | 4KB | 128B |
| [Generic STC15F105](../boards/intel-mcs51/stc15f105.md) | No | STC15F105 | 11MHz | 5KB | 128B |
| [Generic STC15F105E](../boards/intel-mcs51/stc15f105e.md) | No | STC15F105E | 11MHz | 5KB | 128B |
| [Generic STC15F105W](../boards/intel-mcs51/stc15f105w.md) | No | STC15F105W | 11MHz | 5KB | 128B |
| [Generic STC15F201A](../boards/intel-mcs51/stc15f201a.md) | No | STC15F201A | 11MHz | 1KB | 256B |
| [Generic STC15F201EA](../boards/intel-mcs51/stc15f201ea.md) | No | STC15F201EA | 11MHz | 1KB | 256B |
| [Generic STC15F202A](../boards/intel-mcs51/stc15f202a.md) | No | STC15F202A | 11MHz | 2KB | 256B |
| [Generic STC15F202EA](../boards/intel-mcs51/stc15f202ea.md) | No | STC15F202EA | 11MHz | 2KB | 256B |
| [Generic STC15F203A](../boards/intel-mcs51/stc15f203a.md) | No | STC15F203A | 11MHz | 3KB | 256B |
| [Generic STC15F203EA](../boards/intel-mcs51/stc15f203ea.md) | No | STC15F203EA | 11MHz | 3KB | 256B |
| [Generic STC15F204A](../boards/intel-mcs51/stc15f204a.md) | No | STC15F204A | 11MHz | 4KB | 256B |
| [Generic STC15F204EA](../boards/intel-mcs51/stc15f204ea.md) | No | STC15F204EA | 11MHz | 4KB | 256B |
| [Generic STC15F205A](../boards/intel-mcs51/stc15f205a.md) | No | STC15F205A | 11MHz | 5KB | 256B |
| [Generic STC15F205EA](../boards/intel-mcs51/stc15f205ea.md) | No | STC15F205EA | 11MHz | 5KB | 256B |
| [Generic STC15F2K08S2](../boards/intel-mcs51/stc15f2k08s2.md) | No | STC15F2K08S2 | 11MHz | 8KB | 2KB |
| [Generic STC15F2K16S2](../boards/intel-mcs51/stc15f2k16s2.md) | No | STC15F2K16S2 | 11MHz | 16KB | 2KB |
| [Generic STC15F2K24AS](../boards/intel-mcs51/stc15f2k24as.md) | No | STC15F2K24AS | 11MHz | 24KB | 2KB |
| [Generic STC15F2K24S2](../boards/intel-mcs51/stc15f2k24s2.md) | No | STC15F2K24S2 | 11MHz | 24KB | 2KB |
| [Generic STC15F2K32S2](../boards/intel-mcs51/stc15f2k32s2.md) | No | STC15F2K32S2 | 11MHz | 32KB | 2KB |
| [Generic STC15F2K40S2](../boards/intel-mcs51/stc15f2k40s2.md) | No | STC15F2K40S2 | 11MHz | 40KB | 2KB |
| [Generic STC15F2K48S2](../boards/intel-mcs51/stc15f2k48s2.md) | No | STC15F2K48S2 | 11MHz | 48KB | 2KB |
| [Generic STC15F2K52S2](../boards/intel-mcs51/stc15f2k52s2.md) | No | STC15F2K52S2 | 6MHz | 52KB | 2KB |
| [Generic STC15F2K56S2](../boards/intel-mcs51/stc15f2k56s2.md) | No | STC15F2K56S2 | 11MHz | 56KB | 2KB |
| [Generic STC15F2K60S2](../boards/intel-mcs51/stc15f2k60s2.md) | No | STC15F2K60S2 | 11MHz | 60KB | 2KB |
| [Generic STC15F408AD](../boards/intel-mcs51/stc15f408ad.md) | No | STC15F408AD | 11MHz | 8KB | 512B |
| [Generic STC15W100](../boards/intel-mcs51/stc15w100.md) | No | STC15W100 | 11MHz | 512B | 128B |
| [Generic STC15W101](../boards/intel-mcs51/stc15w101.md) | No | STC15W101 | 11MHz | 1KB | 128B |
| [Generic STC15W102](../boards/intel-mcs51/stc15w102.md) | No | STC15W102 | 11MHz | 2KB | 128B |
| [Generic STC15W103](../boards/intel-mcs51/stc15w103.md) | No | STC15W103 | 11MHz | 3KB | 128B |
| [Generic STC15W104](../boards/intel-mcs51/stc15w104.md) | No | STC15W104 | 11MHz | 4KB | 128B |
| [Generic STC15W1K16S](../boards/intel-mcs51/stc15w1k16s.md) | No | STC15W1K16S | 11MHz | 16KB | 1KB |
| [Generic STC15W1K20S](../boards/intel-mcs51/stc15w1k20s.md) | No | STC15W1K20S | 11MHz | 20KB | 1KB |
| [Generic STC15W1K24S](../boards/intel-mcs51/stc15w1k24s.md) | No | STC15W1K24S | 11MHz | 24KB | 1KB |
| [Generic STC15W201S](../boards/intel-mcs51/stc15w201s.md) | No | STC15W201S | 11MHz | 1KB | 256B |
| [Generic STC15W202S](../boards/intel-mcs51/stc15w202s.md) | No | STC15W202S | 11MHz | 2KB | 256B |
| [Generic STC15W203S](../boards/intel-mcs51/stc15w203s.md) | No | STC15W203S | 11MHz | 3KB | 256B |
| [Generic STC15W204S](../boards/intel-mcs51/stc15w204s.md) | No | STC15W204S | 11MHz | 4KB | 256B |
| [Generic STC15W401AS](../boards/intel-mcs51/stc15w401as.md) | No | STC15W401AS | 11MHz | 1KB | 512B |
| [Generic STC15W402AS](../boards/intel-mcs51/stc15w402as.md) | No | STC15W402AS | 11MHz | 2KB | 512B |
| [Generic STC15W404AS](../boards/intel-mcs51/stc15w404as.md) | No | STC15W404AS | 11MHz | 4KB | 512B |
| [Generic STC15W404S](../boards/intel-mcs51/stc15w404s.md) | No | STC15W404S | 11MHz | 4KB | 512B |
| [Generic STC15W408AS](../boards/intel-mcs51/stc15w408as.md) | No | STC15W408AS | 11MHz | 8KB | 512B |
| [Generic STC15W408S](../boards/intel-mcs51/stc15w408s.md) | No | STC15W408S | 11MHz | 8KB | 512B |
| [Generic STC15W410S](../boards/intel-mcs51/stc15w410s.md) | No | STC15W410S | 11MHz | 10KB | 512B |
| [Generic STC15W4K16S4](../boards/intel-mcs51/stc15w4k16s4.md) | No | STC15W4K16S4 | 11MHz | 16KB | 4KB |
| [Generic STC15W4K32S4](../boards/intel-mcs51/stc15w4k32s4.md) | No | STC15W4K32S4 | 11MHz | 32KB | 4KB |
| [Generic STC15W4K40S4](../boards/intel-mcs51/stc15w4k40s4.md) | No | STC15W4K40S4 | 11MHz | 40KB | 4KB |
| [Generic STC15W4K48S4](../boards/intel-mcs51/stc15w4k48s4.md) | No | STC15W4K48S4 | 11MHz | 48KB | 4KB |
| [Generic STC15W4K56S4](../boards/intel-mcs51/stc15w4k56s4.md) | No | STC15W4K56S4 | 11MHz | 56KB | 4KB |
| [Generic STC89C516RD+](../boards/intel-mcs51/stc89c516rd+.md) | No | STC89C516RD+ | 11MHz | 64KB | 1.25KB |
| [Generic STC89C51RC](../boards/intel-mcs51/stc89c51rc.md) | No | STC89C51RC | 11MHz | 4KB | 512B |
| [Generic STC89C52RC](../boards/intel-mcs51/stc89c52rc.md) | No | STC89C52RC | 11MHz | 8KB | 512B |
| [Generic STC89C53RC](../boards/intel-mcs51/stc89c53rc.md) | No | STC89C53RC | 11MHz | 13KB | 512B |
| [Generic STC89C54RD+](../boards/intel-mcs51/stc89c54rd+.md) | No | STC89C54RD+ | 11MHz | 16KB | 1.25KB |
| [Generic STC89C58RD+](../boards/intel-mcs51/stc89c58rd+.md) | No | STC89C58RD+ | 11MHz | 32KB | 1.25KB |
| [Generic STC8A4K16S2A12](../boards/intel-mcs51/stc8a4k16s2a12.md) | No | STC8A4K16S2A12 | 11MHz | 16KB | 4.25KB |
| [Generic STC8A4K32S2A12](../boards/intel-mcs51/stc8a4k32s2a12.md) | No | STC8A4K32S2A12 | 11MHz | 32KB | 4.25KB |
| [Generic STC8A4K60S2A12](../boards/intel-mcs51/stc8a4k60s2a12.md) | No | STC8A4K60S2A12 | 11MHz | 60KB | 4.25KB |
| [Generic STC8A4K64S2A12](../boards/intel-mcs51/stc8a4k64s2a12.md) | No | STC8A4K64S2A12 | 11MHz | 64KB | 4.25KB |
| [Generic STC8A8K16D4](../boards/intel-mcs51/stc8a8k16d4.md) | No | STC8A8K16D4 | 11MHz | 16KB | 8.25KB |
| [Generic STC8A8K16S4A12](../boards/intel-mcs51/stc8a8k16s4a12.md) | No | STC8A8K16S4A12 | 11MHz | 16KB | 8.25KB |
| [Generic STC8A8K32D4](../boards/intel-mcs51/stc8a8k32d4.md) | No | STC8A8K32D4 | 11MHz | 32KB | 8.25KB |
| [Generic STC8A8K32S4A12](../boards/intel-mcs51/stc8a8k32s4a12.md) | No | STC8A8K32S4A12 | 11MHz | 32KB | 8.25KB |
| [Generic STC8A8K60D4](../boards/intel-mcs51/stc8a8k60d4.md) | No | STC8A8K60D4 | 11MHz | 60KB | 8.25KB |
| [Generic STC8A8K60S4A12](../boards/intel-mcs51/stc8a8k60s4a12.md) | No | STC8A8K60S4A12 | 11MHz | 60KB | 8.25KB |
| [Generic STC8A8K64D4](../boards/intel-mcs51/stc8a8k64d4.md) | No | STC8A8K64D4 | 11MHz | 64KB | 8.25KB |
| [Generic STC8A8K64S4A12](../boards/intel-mcs51/stc8a8k64s4a12.md) | No | STC8A8K64S4A12 | 11MHz | 64KB | 8.25KB |
| [Generic STC8C1K08](../boards/intel-mcs51/stc8c1k08.md) | No | STC8C1K08 | 11MHz | 8KB | 1.25KB |
| [Generic STC8C1K12](../boards/intel-mcs51/stc8c1k12.md) | No | STC8C1K12 | 11MHz | 12KB | 1.25KB |
| [Generic STC8C2K16S2](../boards/intel-mcs51/stc8c2k16s2.md) | No | STC8C2K16S2 | 11MHz | 16KB | 2.25KB |
| [Generic STC8C2K16S4](../boards/intel-mcs51/stc8c2k16s4.md) | No | STC8C2K16S4 | 11MHz | 16KB | 2.25KB |
| [Generic STC8C2K32S2](../boards/intel-mcs51/stc8c2k32s2.md) | No | STC8C2K32S2 | 11MHz | 32KB | 2.25KB |
| [Generic STC8C2K32S4](../boards/intel-mcs51/stc8c2k32s4.md) | No | STC8C2K32S4 | 11MHz | 32KB | 2.25KB |
| [Generic STC8C2K60S2](../boards/intel-mcs51/stc8c2k60s2.md) | No | STC8C2K60S2 | 11MHz | 60KB | 2.25KB |
| [Generic STC8C2K60S4](../boards/intel-mcs51/stc8c2k60s4.md) | No | STC8C2K60S4 | 11MHz | 60KB | 2.25KB |
| [Generic STC8C2K64S2](../boards/intel-mcs51/stc8c2k64s2.md) | No | STC8C2K64S2 | 11MHz | 64KB | 2.25KB |
| [Generic STC8C2K64S4](../boards/intel-mcs51/stc8c2k64s4.md) | No | STC8C2K64S4 | 11MHz | 64KB | 2.25KB |
| [Generic STC8F1K08](../boards/intel-mcs51/stc8f1k08.md) | No | STC8F1K08 | 11MHz | 8KB | 1.25KB |
| [Generic STC8F1K08S](../boards/intel-mcs51/stc8f1k08s.md) | No | STC8F1K08S | 11MHz | 8KB | 1.25KB |
| [Generic STC8F1K08S2](../boards/intel-mcs51/stc8f1k08s2.md) | No | STC8F1K08S2 | 11MHz | 8KB | 1.25KB |
| [Generic STC8F1K08S2A10](../boards/intel-mcs51/stc8f1k08s2a10.md) | No | STC8F1K08S2A10 | 11MHz | 8KB | 1.25KB |
| [Generic STC8F1K17](../boards/intel-mcs51/stc8f1k17.md) | No | STC8F1K17 | 11MHz | 17KB | 1.25KB |
| [Generic STC8F1K17S2](../boards/intel-mcs51/stc8f1k17s2.md) | No | STC8F1K17S2 | 11MHz | 17KB | 1.25KB |
| [Generic STC8F2K08S2](../boards/intel-mcs51/stc8f2k08s2.md) | No | STC8F2K08S2 | 11MHz | 8KB | 2.25KB |
| [Generic STC8F2K16S2](../boards/intel-mcs51/stc8f2k16s2.md) | No | STC8F2K16S2 | 11MHz | 16KB | 2.25KB |
| [Generic STC8F2K16S4](../boards/intel-mcs51/stc8f2k16s4.md) | No | STC8F2K16S4 | 11MHz | 16KB | 2.25KB |
| [Generic STC8F2K32S2](../boards/intel-mcs51/stc8f2k32s2.md) | No | STC8F2K32S2 | 11MHz | 32KB | 2.25KB |
| [Generic STC8F2K32S4](../boards/intel-mcs51/stc8f2k32s4.md) | No | STC8F2K32S4 | 11MHz | 32KB | 2.25KB |
| [Generic STC8F2K60S2](../boards/intel-mcs51/stc8f2k60s2.md) | No | STC8F2K60S2 | 11MHz | 60KB | 2.25KB |
| [Generic STC8F2K60S4](../boards/intel-mcs51/stc8f2k60s4.md) | No | STC8F2K60S4 | 11MHz | 60KB | 2.25KB |
| [Generic STC8F2K64S2](../boards/intel-mcs51/stc8f2k64s2.md) | No | STC8F2K64S2 | 11MHz | 64KB | 2.25KB |
| [Generic STC8F2K64S4](../boards/intel-mcs51/stc8f2k64s4.md) | No | STC8F2K64S4 | 11MHz | 64KB | 2.25KB |
| [Generic STC8G1K08](../boards/intel-mcs51/stc8g1k08.md) | No | STC8G1K08 | 11MHz | 8KB | 1.25KB |
| [Generic STC8G1K08A](../boards/intel-mcs51/stc8g1k08a.md) | No | STC8G1K08A | 11MHz | 8KB | 1.25KB |
| [Generic STC8G1K08T](../boards/intel-mcs51/stc8g1k08t.md) | No | STC8G1K08T | 11MHz | 8KB | 1.25KB |
| [Generic STC8G1K12](../boards/intel-mcs51/stc8g1k12.md) | No | STC8G1K12 | 11MHz | 12KB | 1.25KB |
| [Generic STC8G1K12A](../boards/intel-mcs51/stc8g1k12a.md) | No | STC8G1K12A | 11MHz | 12KB | 1.25KB |
| [Generic STC8G1K17](../boards/intel-mcs51/stc8g1k17.md) | No | STC8G1K17 | 11MHz | 17KB | 1.25KB |
| [Generic STC8G1K17A](../boards/intel-mcs51/stc8g1k17a.md) | No | STC8G1K17A | 11MHz | 17KB | 1.25KB |
| [Generic STC8G1K17T](../boards/intel-mcs51/stc8g1k17t.md) | No | STC8G1K17T | 11MHz | 17KB | 1.25KB |
| [Generic STC8G2K16S2](../boards/intel-mcs51/stc8g2k16s2.md) | No | STC8G2K16S2 | 11MHz | 16KB | 2.25KB |
| [Generic STC8G2K16S4](../boards/intel-mcs51/stc8g2k16s4.md) | No | STC8G2K16S4 | 11MHz | 16KB | 2.25KB |
| [Generic STC8G2K32S2](../boards/intel-mcs51/stc8g2k32s2.md) | No | STC8G2K32S2 | 11MHz | 32KB | 2.25KB |
| [Generic STC8G2K32S4](../boards/intel-mcs51/stc8g2k32s4.md) | No | STC8G2K32S4 | 11MHz | 32KB | 2.25KB |
| [Generic STC8G2K60S2](../boards/intel-mcs51/stc8g2k60s2.md) | No | STC8G2K60S2 | 11MHz | 60KB | 2.25KB |
| [Generic STC8G2K60S4](../boards/intel-mcs51/stc8g2k60s4.md) | No | STC8G2K60S4 | 11MHz | 60KB | 2.25KB |
| [Generic STC8G2K64S2](../boards/intel-mcs51/stc8g2k64s2.md) | No | STC8G2K64S2 | 11MHz | 64KB | 2.25KB |
| [Generic STC8G2K64S4](../boards/intel-mcs51/stc8g2k64s4.md) | No | STC8G2K64S4 | 11MHz | 64KB | 2.25KB |
| [Generic STC8H04](../boards/intel-mcs51/stc8h04.md) | No | STC8H04 | 11MHz | 4KB | 256B |
| [Generic STC8H04A10](../boards/intel-mcs51/stc8h04a10.md) | No | STC8H04A10 | 11MHz | 4KB | 256B |
| [Generic STC8H1K08](../boards/intel-mcs51/stc8h1k08.md) | No | STC8H1K08 | 11MHz | 8KB | 1.25KB |
| [Generic STC8H1K08S2](../boards/intel-mcs51/stc8h1k08s2.md) | No | STC8H1K08S2 | 11MHz | 8KB | 1.25KB |
| [Generic STC8H1K08S2A10](../boards/intel-mcs51/stc8h1k08s2a10.md) | No | STC8H1K08S2A10 | 11MHz | 8KB | 1.25KB |
| [Generic STC8H1K12](../boards/intel-mcs51/stc8h1k12.md) | No | STC8H1K12 | 11MHz | 12KB | 1.25KB |
| [Generic STC8H1K16](../boards/intel-mcs51/stc8h1k16.md) | No | STC8H1K16 | 11MHz | 16KB | 1.25KB |
| [Generic STC8H1K16S2](../boards/intel-mcs51/stc8h1k16s2.md) | No | STC8H1K16S2 | 11MHz | 16KB | 1.25KB |
| [Generic STC8H1K16S2A10](../boards/intel-mcs51/stc8h1k16s2a10.md) | No | STC8H1K16S2A10 | 11MHz | 16KB | 1.25KB |
| [Generic STC8H1K17](../boards/intel-mcs51/stc8h1k17.md) | No | STC8H1K17 | 11MHz | 17KB | 1.25KB |
| [Generic STC8H1K24](../boards/intel-mcs51/stc8h1k24.md) | No | STC8H1K24 | 11MHz | 24KB | 1.25KB |
| [Generic STC8H1K28](../boards/intel-mcs51/stc8h1k28.md) | No | STC8H1K28 | 11MHz | 28KB | 1.25KB |
| [Generic STC8H1K32S2](../boards/intel-mcs51/stc8h1k32s2.md) | No | STC8H1K32S2 | 11MHz | 32KB | 1.25KB |
| [Generic STC8H1K32S2A10](../boards/intel-mcs51/stc8h1k32s2a10.md) | No | STC8H1K32S2A10 | 11MHz | 32KB | 1.25KB |
| [Generic STC8H1K33](../boards/intel-mcs51/stc8h1k33.md) | No | STC8H1K33 | 11MHz | 33KB | 1.25KB |
| [Generic STC8H1K64S2A10](../boards/intel-mcs51/stc8h1k64s2a10.md) | No | STC8H1K64S2A10 | 11MHz | 32KB | 1.25KB |
| [Generic STC8H2K32T](../boards/intel-mcs51/stc8h2k32t.md) | No | STC8H2K32T | 11MHz | 32KB | 2.25KB |
| [Generic STC8H2K48T](../boards/intel-mcs51/stc8h2k48t.md) | No | STC8H2K48T | 11MHz | 48KB | 2.25KB |
| [Generic STC8H2K60T](../boards/intel-mcs51/stc8h2k60t.md) | No | STC8H2K60T | 11MHz | 60KB | 2.25KB |
| [Generic STC8H2K64T](../boards/intel-mcs51/stc8h2k64t.md) | No | STC8H2K64T | 11MHz | 64KB | 2.25KB |
| [Generic STC8H3K32S2](../boards/intel-mcs51/stc8h3k32s2.md) | No | STC8H3K32S2 | 11MHz | 32KB | 3.25KB |
| [Generic STC8H3K32S4](../boards/intel-mcs51/stc8h3k32s4.md) | No | STC8H3K32S4 | 11MHz | 32KB | 3.25KB |
| [Generic STC8H3K48S2](../boards/intel-mcs51/stc8h3k48s2.md) | No | STC8H3K48S2 | 11MHz | 32KB | 3.25KB |
| [Generic STC8H3K48S4](../boards/intel-mcs51/stc8h3k48s4.md) | No | STC8H3K48S4 | 11MHz | 48KB | 3.25KB |
| [Generic STC8H3K60S2](../boards/intel-mcs51/stc8h3k60s2.md) | No | STC8H3K60S2 | 11MHz | 60KB | 3.25KB |
| [Generic STC8H3K60S4](../boards/intel-mcs51/stc8h3k60s4.md) | No | STC8H3K60S4 | 11MHz | 60KB | 3.25KB |
| [Generic STC8H3K64S2](../boards/intel-mcs51/stc8h3k64s2.md) | No | STC8H3K64S2 | 11MHz | 64KB | 3.25KB |
| [Generic STC8H3K64S4](../boards/intel-mcs51/stc8h3k64s4.md) | No | STC8H3K64S4 | 11MHz | 64KB | 3.25KB |
| [Generic STC8H4K32LCD](../boards/intel-mcs51/stc8h4k32lcd.md) | No | STC8H4K32LCD | 11MHz | 32KB | 4.25KB |
| [Generic STC8H4K32TLCD](../boards/intel-mcs51/stc8h4k32tlcd.md) | No | STC8H4K32TLCD | 11MHz | 32KB | 4.25KB |
| [Generic STC8H4K32TLR](../boards/intel-mcs51/stc8h4k32tlr.md) | No | STC8H4K32TLR | 11MHz | 32KB | 4.25KB |
| [Generic STC8H4K48LCD](../boards/intel-mcs51/stc8h4k48lcd.md) | No | STC8H4K48LCD | 11MHz | 48KB | 4.25KB |
| [Generic STC8H4K48TLCD](../boards/intel-mcs51/stc8h4k48tlcd.md) | No | STC8H4K48TLCD | 11MHz | 48KB | 4.25KB |
| [Generic STC8H4K48TLR](../boards/intel-mcs51/stc8h4k48tlr.md) | No | STC8H4K48TLR | 11MHz | 48KB | 4.25KB |
| [Generic STC8H4K60LCD](../boards/intel-mcs51/stc8h4k60lcd.md) | No | STC8H4K60LCD | 11MHz | 60KB | 4.25KB |
| [Generic STC8H4K60TLCD](../boards/intel-mcs51/stc8h4k60tlcd.md) | No | STC8H4K60TLCD | 11MHz | 60KB | 4.25KB |
| [Generic STC8H4K60TLR](../boards/intel-mcs51/stc8h4k60tlr.md) | No | STC8H4K60TLR | 11MHz | 60KB | 4.25KB |
| [Generic STC8H4K64LCD](../boards/intel-mcs51/stc8h4k64lcd.md) | No | STC8H4K64LCD | 11MHz | 64KB | 4.25KB |
| [Generic STC8H4K64TLCD](../boards/intel-mcs51/stc8h4k64tlcd.md) | No | STC8H4K64TLCD | 11MHz | 64KB | 4.25KB |
| [Generic STC8H4K64TLR](../boards/intel-mcs51/stc8h4k64tlr.md) | No | STC8H4K64TLR | 11MHz | 64KB | 4.25KB |
| [Generic STC8H8K32U](../boards/intel-mcs51/stc8h8k32u.md) | No | STC8H8K32U | 11MHz | 32KB | 8.25KB |
| [Generic STC8H8K48U](../boards/intel-mcs51/stc8h8k48u.md) | No | STC8H8K48U | 11MHz | 48KB | 8.25KB |
| [Generic STC8H8K60U](../boards/intel-mcs51/stc8h8k60u.md) | No | STC8H8K60U | 11MHz | 60KB | 8.25KB |
| [Generic STC8H8K64U](../boards/intel-mcs51/stc8h8k64u.md) | No | STC8H8K64U | 11MHz | 64KB | 8.25KB |

### WCH

| Name | Debug | MCU | Frequency | Flash | RAM |
|---|---|---|---|---|---|
| [CH559](../boards/intel-mcs51/ch559.md) | No | CH559 | 12MHz | 64KB | 6.25KB |

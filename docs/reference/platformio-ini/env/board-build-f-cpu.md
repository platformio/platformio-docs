<a id="projectconf-board-build-f-cpu"></a>

# `board_build.f_cpu` {#board-build-f-cpu}

Type: `Number` | Multiple: `No`

The option `board_build.f_cpu` is used to define MCU frequency (Hertz, Clock). A format of this option is `C-like long integer` value with `L` suffix. The 1 Hertz is equal to `1L`, then 16 MHz (Mega Hertz) is equal to `16000000L`.

The full list of `board_build.f_cpu` for the popular embedded platforms you can find in *Boards* section of [Development Platforms](../../../hardware/platforms/index.md). See "Frequency" column.

:::note

This option doesn't make any changes to real clock settings on hardware. You should specify a `board_build.f_cpu` value  if you have changed a target's clock frequency so that the underlying software will be configured accordingly to match the change.

:::

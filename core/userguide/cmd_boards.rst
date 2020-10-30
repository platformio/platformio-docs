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

.. _cmd_boards:

pio boards
==========

.. contents::

Usage
-----

.. code-block:: bash

    pio boards [OPTIONS] [FILTER]

Description
-----------

List pre-configured Embedded Boards

Options
~~~~~~~

.. program:: pio boards

.. option::
    --installed

List boards only from the installed platforms

.. option::
    --json-output

Return the output in `JSON <http://en.wikipedia.org/wiki/JSON>`_ format

Examples
--------

1. Show all available pre-configured embedded boards

.. code-block:: bash

    > pio boards

    Platform: atmelavr
    ---------------------------------------------------------------------------
    ID                    MCU           Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    btatmega168           atmega168     16MHz     14K    1K    Arduino BT ATmega168
    btatmega328           atmega328p    16MHz     28K    2K    Arduino BT ATmega328
    diecimilaatmega168    atmega168     16MHz     14K    1K    Arduino Duemilanove or Diecimila ATmega168
    diecimilaatmega328    atmega328p    16MHz     30K    2K    Arduino Duemilanove or Diecimila ATmega328
    esplora               atmega32u4    16MHz     28K    2K    Arduino Esplora
    ethernet              atmega328p    16MHz     31K    2K    Arduino Ethernet
    ...

2. Filter Arduino-based boards

.. code-block:: bash

    > pio boards arduino

    Platform: atmelavr
    ---------------------------------------------------------------------------
    ID                    MCU           Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    btatmega168           atmega168     16MHz     14K    1K    Arduino BT ATmega168
    btatmega328           atmega328p    16MHz     28K    2K    Arduino BT ATmega328
    diecimilaatmega168    atmega168     16MHz     14K    1K    Arduino Duemilanove or Diecimila ATmega168
    diecimilaatmega328    atmega328p    16MHz     30K    2K    Arduino Duemilanove or Diecimila ATmega328
    esplora               atmega32u4    16MHz     28K    2K    Arduino Esplora
    ethernet              atmega328p    16MHz     31K    2K    Arduino Ethernet
    ...


3. Filter mbed-enabled boards

.. code-block:: bash

    > pio boards mbed

    Platform: freescalekinetis
    ---------------------------------------------------------------------------
    ID                    MCU            Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    frdm_k20d50m          mk20dx128vlh5  48MHz     128K   16K   Freescale Kinetis FRDM-K20D50M
    frdm_k22f             mk22fn512vlh12 120MHz    512K   128K  Freescale Kinetis FRDM-K22F
    ...

    Platform: nordicnrf51
    ---------------------------------------------------------------------------
    ID                    MCU            Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    wallBotBLE            nrf51822       16MHz     128K   16K   JKSoft Wallbot BLE
    nrf51_dk              nrf51822       32MHz     256K   32K   Nordic nRF51-DK
    ...

    Platform: nxplpc
    ---------------------------------------------------------------------------
    ID                    MCU            Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    blueboard_lpc11u24    lpc11u24       48MHz     32K    8K    BlueBoard-LPC11U24
    dipcortexm0           lpc11u24       50MHz     32K    8K    DipCortex M0
    lpc11u35              lpc11u35       48MHz     64K    10K   EA LPC11U35 QuickStart Board
    ...

    Platform: ststm32
    ---------------------------------------------------------------------------
    ID                    MCU            Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    disco_f401vc          stm32f401vct6  84MHz     256K   64K   32F401CDISCOVERY
    nucleo_f030r8         stm32f030r8t6  48MHz     64K    8K    ST Nucleo F030R8
    ...

4. Filter boards which are based on ``ATmega168`` MCU

.. code-block:: bash

    > pio boards atmega168

    Platform: atmelavr
    ---------------------------------------------------------------------------
    ID                    MCU           Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    btatmega168           atmega168     16MHz     14K    1K    Arduino BT ATmega168
    diecimilaatmega168    atmega168     16MHz     14K    1K    Arduino Duemilanove or Diecimila ATmega168
    miniatmega168         atmega168     16MHz     14K    1K    Arduino Mini ATmega168
    atmegangatmega168     atmega168     16MHz     14K    1K    Arduino NG or older ATmega168
    nanoatmega168         atmega168     16MHz     14K    1K    Arduino Nano ATmega168
    pro8MHzatmega168      atmega168     8MHz      14K    1K    Arduino Pro or Pro Mini ATmega168 (3.3V, 8 MHz)
    pro16MHzatmega168     atmega168     16MHz     14K    1K    Arduino Pro or Pro Mini ATmega168 (5V, 16 MHz)
    lilypadatmega168      atmega168     8MHz      14K    1K    LilyPad Arduino ATmega168
    168pa16m              atmega168p    16MHz     15K    1K    Microduino Core (Atmega168PA@16M,5V)
    168pa8m               atmega168p    8MHz      15K    1K    Microduino Core (Atmega168PA@8M,3.3V)

5. Show boards by :ref:`platform_timsp430`

.. code-block:: bash

    > pio boards timsp430

    Platform: timsp430
    ---------------------------------------------------------------------------
    ID                    MCU           Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    lpmsp430fr5739        msp430fr5739  16MHz     15K    1K    FraunchPad w/ msp430fr5739
    lpmsp430f5529         msp430f5529   16MHz     128K   1K    LaunchPad w/ msp430f5529 (16MHz)
    lpmsp430f5529_25      msp430f5529   25MHz     128K   1K    LaunchPad w/ msp430f5529 (25MHz)
    lpmsp430fr5969        msp430fr5969  8MHz      64K    1K    LaunchPad w/ msp430fr5969
    lpmsp430g2231         msp430g2231   1MHz      2K     128B   LaunchPad w/ msp430g2231 (1MHz)
    lpmsp430g2452         msp430g2452   16MHz     8K     256B   LaunchPad w/ msp430g2452 (16MHz)
    lpmsp430g2553         msp430g2553   16MHz     16K    512B   LaunchPad w/ msp430g2553 (16MHz)

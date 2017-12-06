..  Copyright (c) 2014-atualmente <contact@platformio.org>
    Licenciado sobre a Licença Apache, Versão 2.0 (a "Licença");
    você não pode usar este arquivo exceto em conformidade com a Licença.
    Você pode conseguir uma cópia desta Licença em
       http://www.apache.org/licenses/LICENSE-2.0.
    A menos que seja exigido lei aplicável ou acordado por escrito, o software
    distribuído sobre a Licença é distribuído "COMO ESTÁ",
    SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressa ou implícita.
    Consulte a Licença para o idioma específico que rege as permissões e
    limitações sob a Licença.

.. _projectconf:

Arquivo de Configuração do Projeto ``platformio.ini``
===================================================

O arquivo de configuração do projeto tem o nome ``platformio.ini``. Este é um
arquivo `INI-style <http://en.wikipedia.org/wiki/INI_file>`_.

``platformio.ini`` tem seções (cada uma denotada por um ``[header]``)
par chave / valor dentro das seções. Linhas que iniciam com ``;``
são ignoradas e possivelmente usadas como comentários.

Opções multivaloradas podem ser especificadas de 2 formas:

1. Dividindo os valores com ", " (vírgula + espaço)
2. Use formato multilinha, onde cada linha pode iniciar com 2 espaços (no mínimo)

**Exemplo**

.. code-block:: ini

    [platformio]
    env_default = nodemcuv2

    ; You MUST inject these options into [env:] section
    ; using ${common_env_data.***} (see below)
    [common_env_data]
    build_flags =
        -D VERSION=1.2.3
        -D DEBUG=1
    lib_deps_builtin =
        SPI
        Wire
    lib_deps_external =
        ArduinoJson@~5.6,!=5.4
        https://github.com/gioblu/PJON.git#v2.0
        https://github.com/adafruit/DHT-sensor-library/archive/master.zip

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2

    ; Build options
    build_flags =
        ${common_env_data.build_flags}
        -DSSID_NAME=HELLO
        -DSSID_PASWORD=WORLD

    ; Library options
    lib_deps =
        ${common_env_data.lib_deps_builtin}
        ${common_env_data.lib_deps_external}
        https://github.com/me-no-dev/ESPAsyncTCP.git
        PubSubClient@2.6
        OneWire

    ; Serial Monitor options
    monitor_baud = 115200

    ; Unit Testing options
    test_ignore = test_desktop

    [env:bluepill_f103c8]
    platform = ststm32
    framework = arduino
    board = bluepill_f103c8

    ; Build options
    build_flags = ${common_env_data.build_flags}

    ; Library options
    lib_deps =
        ${common.lib_deps_external}

    ; Debug options
    debug_tool = custom
    debug_server =
        JLinkGDBServer
        -singlerun
        -if
        SWD
        -select
        USB
        -port
        2331
        -device
        STM32F103C8

    ; Unit Testing options
    test_ignore = test_desktop

Existem 2 sessões de sistema reservadas:

* :ref:`piocore` settings: :ref:`projectconf_section_platformio`
* Environment settings: :ref:`projectconf_section_env`

As outras sessões podem ser usadas por usuários, por exemplo, para
:ref:`projectconf_dynamic_vars`. As sessões e seus valores permitidos são
descritos abaixo.

.. toctree::
    :maxdepth: 2

    [platformio] <projectconf/section_platformio>
    [env] <projectconf/section_env>
    projectconf/dynamic_variables
    projectconf/examples

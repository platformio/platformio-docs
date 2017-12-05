..  PlatformIO Copyright (c) 2014-atualmente <contact@platformio.org>
    Licenciado sobre a Licença Apache, Versão 2.0 (a "Licença");
    você não pode usar este arquivo exceto em conformidade com a Licença.
    Você pode conseguir uma cópia desta Licença em
       http://www.apache.org/licenses/LICENSE-2.0.
    A menos que seja exigido lei aplicável ou acordado por escrito, o software
    distribuído sobre a Licença é distribuído "COMO ESTÁ",
    SEM GARANTIAS OU CONDIÇÕES DE QUALQUER TIPO, expressa ou implícita.
    Consulte a Licença para o idioma específico que rege as permissões e
    limitações sob a Licença.

.. _quickstart:

Início Rápido
=============

Este tutorial introduz você ao básico do workflow de :ref:`piocore` Interface de Linha
de Comando (CLI) e mostra um simples processo de criação de um projeto cross-platform
`Blink`. Encerrando você pode ter uma compreensão geral de como trabalhar com
o desenvolvimento de múltiplas plataformas e placas embarcadas.

Configurando o Projeto
----------------------

:ref:`piocore` provê um comando :ref:`cmd_init` especial para configurar seus projetos.
Isso permite iniciar um novo projeto vazio ou atualizar um existe com novos dados.

Além disso, :ref:`cmd_init` pode ser usado para :ref:`ide`. Isso significa que você
estará apto a importar um projeto PlatformIO recém-gerado usando sua IDE favorita e
extendê-lo com instrumentos profissionais para desenvolvimento em IOT.

Esse tutorial é baseado nos próximas placas embarcadas populares e desenvolvimento de
plataformas usando *Frameworks para Arduíno*:


.. list-table::
    :header-rows:  1

    * - Plataforma
      - Placa
      - Framework

    * - Atmel AVR
      - Arduino Uno (8-bit ATmega328P)
      - Arduino Wiring-based Framework

    * - Espressif
      - NodeMCU 1.0 (32-bit ESP8266)
      - Arduino Wiring-based Framework

    * - Teensy
      - Teensy 3.1 (32-bit ARM MK20DX256)
      - Arduino Wiring-based Framework

Identificador da Placa
----------------------

o comando :ref:`cmd_init` requer um identificador específico (ID/TYPE). Isso pode
ser encontrado usando `Embedded Boards Explorer <http://platformio.org/boards>`
ou o comando :ref:`cmd_boards`. Por exemplo, usando :ref:`cmd_boards` vamos tentar
encontrar placas Teensy:

.. code-block:: bash

    > platformio boards teensy

    Platform: teensy
    ---------------------------------------------------------------------------
    Type                  MCU            Frequency  Flash   RAM    Name
    ---------------------------------------------------------------------------
    teensy20              atmega32u4     16Mhz     31kB    2.5kB  Teensy 2.0
    teensy30              mk20dx128      48Mhz     128kB   16kB   Teensy 3.0
    teensy31              mk20dx256      72Mhz     256kB   64kB   Teensy 3.1 / 3.2
    teensylc              mkl26z64       48Mhz     62kB    8kB    Teensy LC
    teensy20pp            at90usb1286    16Mhz     127kB   8kB    Teensy++ 2.0

De acordo com a tabela acima o ID/TYPE para Teensy 3.1 é ``teensy31``. Além disso,
o ID para Arduino UNO é ``uno`` e para NodeMCU 1.0 (ESP-12E Module)
é ``nodemcuv2``.

Inicializar o Projeto
---------------------

O ecossistema PlatformIO contém um grande banco de dados com alterações pré configuradas
para as placas embarcadas mais populares. Isso te ajuda a esquecer da instalação de várias
ferramentas, escrevendo apenas scripts de build ou configurando o processo de upload. Apenas informe
PlatformIO e o ID da placa e você pode receber um projeto completo com
instrumentos pré-instalados para um desenvolvimento profissional.

1.  Crie uma pasta vazia onde você vai inicializar o novo projeto PlatformIO.
    Então abra o terminal do sistema e mude o diretório assim:

    .. code-block:: bash

        # cria nova pasta
        > mkdir path_to_the_new_directory

        # acessa ela
        > cd path_to_the_new_directory

2.  Inicialize o projeto para as placas mencionadas acima (você pode especificar mais
    de uma placa nesse momento):

    .. code-block:: bash

        > platformio init --board uno --board nodemcuv2 --board teensy31

        A atual pasta de trabalho *** pode ser usada para o novo projeto.
        Você pode especificar outra pasta de projeto com o comando
        `platformio init -d %PATH_TO_THE_PROJECT_DIR%`.

        Os próximos arquivos/pastas podem ser criadas em ***
        platformio.ini - Arquivo de Configuração do Projeto. |-> Por faver, edite-me <-|
        src - Coloque seus arquivos de código aqui
        lib - Coloque aqui projetos específicos, bibliotecas (privados)
        Você deseja continuar? [y/N]: y
        O Projeto foi inicializado com sucesso!
        Comandos mais usados:
        `platformio run` - process/build do projeto para a pasta atual
        `platformio run --target upload` ou `platformio run -t upload` - atualiza o firmware para a placa embarcada
        `platformio run --target clean` - limpa o projeto (remove arquivos compilados)


Parabéns! Você criou o primeiro Projeto baseado em PlatformIO com a
seguinte estrutura:

* :ref:`projectconf`
* ``src`` pasta onde você pode encontrar o código fonte
  (``*.h, *.c, *.cpp, *.S, *.ino, etc.``)
* ``lib`` pasta pode ser criada para projetos e bibliotecas específicos (privados).
  Mais detalhes estão localizados no arquivo ``lib/readme.txt``.
* Diversos arquivos para VCS e suporte a :ref:`ci`.


.. note::
    Se você precisar adicionar uma nova placa para um projeto existente use
    :ref:`cmd_init` novamente.


O resultado gerado para ``platformio.ini``:

.. code-block:: ini

    ; PlatformIO Project Configuration File
    ;
    ;   Build options: build flags, source filter, extra scripting
    ;   Upload options: custom port, speed and extra flags
    ;   Library options: dependencies, extra library storages
    ;
    ; Please visit documentation for the other options and examples
    ; http://docs.platformio.org/page/projectconf.html

    [env:uno]
    platform = atmelavr
    framework = arduino
    board = uno

    [env:nodemcuv2]
    platform = espressif8266
    framework = arduino
    board = nodemcuv2

    [env:teensy31]
    platform = teensy
    framework = arduino
    board = teensy31


Agora, nós precisamos criar o arquivo ``main.cpp`` e colocá-lo na pasta ``src`` de seu
novo projeto criado.

O conteúdo de ``src/main.cpp``:

.. code-block:: cpp

    /**
     * Blink
     *
     * Turns on an LED on for one second,
     * then off for one second, repeatedly.
     */
    #include "Arduino.h"

    #ifndef LED_BUILTIN
    #define LED_BUILTIN 13
    #endif

    void setup()
    {
      // initialize LED digital pin as an output.
      pinMode(LED_BUILTIN, OUTPUT);
    }

    void loop()
    {
      // turn the LED on (HIGH is the voltage level)
      digitalWrite(LED_BUILTIN, HIGH);

      // wait for a second
      delay(1000);

      // turn the LED off by making the voltage LOW
      digitalWrite(LED_BUILTIN, LOW);

       // wait for a second
      delay(1000);
    }


A estrutura final do projeto:

.. code-block:: bash

    project_dir
    ├── lib
    │   └── readme.txt
    ├── platformio.ini
    └── src
        └── main.cpp


Processos do Projeto
--------------------

:ref:`piocore` provê um comando especial :ref:`cmd_run` para o processo do projeto.
Se você chamar sem qualquer argumento, PlatformIO faz o build do processo com todos
os ambientes do projeto (que foram criadas com cada placa especificada acima).
Estes são alguns dos comandos mais usados:

* ``platformio run``. Processa (faz o build) de todos os ambientes especificados em
  :ref:`projectconf`
* ``platformio run --target upload``. Faz o build do projeto e atualiza a placa para
todos os dispositivos especificados em :ref:`projectconf`
* ``platformio run --target clean``. Limpa o projeto (apaga objetos compilados)
* ``platformio run -e uno``. Processa o ambiente ``uno``
* ``platformio run -e uno -t upload``. Faz o build do projeto somente para ``uno``
e atualiza o firmware.

Por favor siga para a documentação de :option:`platformio run --target` para outros objetivos.

Finalmente, a demonstração pode mostrar o projeto fazendo o build e atualizando o firmware para
Arduino Uno:

.. image:: _static/platformio-demo-wiring.gif

Leitura futura
--------------

* `Exemplos de projetos <https://github.com/platformio/platformio-examples/tree/develop>`_
* :ref:`userguide` para os comandos :ref:`piocore`.

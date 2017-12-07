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

.. _what_is_pio:

O que é PlatformIO?
===================

.. contents:: Conteúdos
    :local:

Publicação sobre PlatformIO
---------------------------

"Microcontroladores diferentes normalmente tem ferramentas de desenvolvimento diferente .
Para o caso do Arduino dependem da Arduino IDE. Usuários mais avançados configuram diferentes
interfaces gráficas como Eclipse para uma melhor administração do projeto. As vezes
isso pode ser difícil para dar continuidade com diferentes microcontroladores e ferramentas. Você
provavelmente pensa que unificar as ferramentas de desenvolvimento pode ser ótimo. Bem,
é para isso o ecosistema open source PlatformIO.

Esta é uma plataforma de construção de código e administrador de biblioteca com plataforma como
Arduino ou suporte MBED. Eles cuidaram do conjunto de ferramentas, debbugers, frameworks
para trabalhar nas mais populares plataformas como Windows, Mac e Linux. Ele suporta
mais de 200 placas de desenvolvimento com mais de 15 plataformas de desenvolvimento
e 10 frameworks. As placas mais populares estão cobertas. Eles fizeramum árduo trabalho
na organização e administração de centena de bibliotecas que podem ser incluídas
facilmente em seu projeto. PlatformIO inicialmente foi desenvolvido com a filosofia de linha de comando.
Isso foi com sucesso usado com outras IDE's como Eclipse ou Visual Studio.
Recentemente nós lançamos uma versão construída na IDE base do Editor de texto Atom", -
[Embarcados]_.

Prêmios
-------

PlatformIO foi indicado para este ano o `melhor Software e ferramentas em 2015/16 IoT Awards <http://www.postscapes.com/2015-16/best-iot-software-and-tools/>`_.

O Problema
----------

* O principal problema que afasta as pessoas do mundo embarcado é um complicado
  processo de no fornecimento proprietário para o desenvolvimento de software para uma MCU/placa: conjunto de ferramentas,
  IDE de fornecedor proprietário (algumas vezes não é free) entre outros,
  para conseguir um computador com SO onde esse software é suportado.
* Múltiplas plataformas (MCUs, placas) requerem diferentes conjuntos de ferramentas,
  IDEs, etc, e respectivamente, passar tempo no aprendizado de novos ambientes de desenvolvimento.
* Procurar bibliotecas próprias e exemplos de código mostrando como usar populares
  sensores, atuadores, etc.
* Compartilhando projetos embarcados entre os membros da equipe, independentemente do
  sistema operacional eles trabalham.

Visão Geral
-----------

PlatformIO independente de plataforma estará rodando. De fato,
o único requerimento é Python, que existe praticamente em todos os lugares. O que
significa que projetos PlatformIO podem ser facilmente movidos de um computador para
outro, bem como isso PlatformIO permite o fácil compartilhamento de projetos
entre membros da equipe, independentemente do sistema operacional que eles prefiram trabalhar.
Além disso, PlatformIO pode rodar não somente nos comumente usados desktops/laptops
mas também nos servidores sem o sistema X Window. Enquanto PaltformIO é por si só
uma aplicação console, ele também pode ser usado em combinação com uma
:ref:`ide` favorita ou editor de texto como :ref:`ide_atom`, :ref:`ide_clion`,
:ref:`ide_eclipse`, :ref:`ide_emacs`, :ref:`ide_netbeans`, :ref:`ide_qtcreator`,
:ref:`ide_sublimetext`, :ref:`ide_vim`, :ref:`ide_visualstudio`,
:ref:`ide_vscode`, etc.

Bem, PlatformIO pode rodar em diferentes sistemas operacionais. Mas mais
importante, para finalmente uma perspectiva de desenvolvimento, tem uma lista de placas e MCUs
suportadas. Para ser breve: PlatformIO suporta aproximadamente 200
`Placas Embarcadas <http://platformio.org/boards>`_ e a maioria das plataformas -
:ref:`platforms`.

O usuário DEVE ter uma escolha
------------------------------

* Decida qual sistema operacional procura rodar o processo de desenvolvimento.
  Você pode até usar um SO em casa e outro no trabalho.
* Escolha qual editor usar para escrever o código. Pode ser um editor bem simples
  ou uma poderosa :ref:`ide`.
* Foco no desenvolvimento de código, significativamente simplificando o suporte para as
  :ref:`platforms` e MCUs.

Como isso funciona?
-------------------

Sem se aprofundar em detalhes de implementação do PlatformIO, o ciclo de trabalho do
desenvolvimento de projeto usando PlatformIO é o seguinte:

* Usuários escolhem as placas de interesse em :ref:`projectconf`
* Baseado na lista de placas, PlatformIO baixa o conjunto de ferramentas e
  as instala automaticamente.
* Usuários desenvolvem o código e PlatformIO dá a certeza que ele será compilado, preparado
  e atualizado para todas as placas de interesse.


.. [Embarcados] Embedds.com: `Desenvolva facilmente com o ecossistema PlatformIO <http://www.embedds.com/develop-easier-with-platformio-ecosystem/>`_

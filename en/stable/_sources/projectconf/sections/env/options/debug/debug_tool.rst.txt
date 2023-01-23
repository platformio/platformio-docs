.. _projectconf_debug_tool:

``debug_tool``
--------------

Type: ``String`` | Multiple: ``No``

A name of debugging tool. This option is useful when board supports more than
one debugging tool (adapter, probe) or you want to create :ref:`debugging_tool_custom`
debugging configuration.

See available tools in :ref:`debugging_tools`.

**Example**

.. code-block:: ini

    [env:debug]
    platform = ...
    board = ...
    debug_tool = custom
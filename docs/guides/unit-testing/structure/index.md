---
description: Organize unit tests in a PlatformIO project - test suites, hierarchy, shared code and best practices.
---

# Project structure {#project-structure}

Tests live in the project's [`test`](../../../reference/platformio-ini/platformio/test-dir.md)
folder. Each folder whose name starts with `test_` is a test suite: it is built
and run on its own. If there are no `test_*` folders, the whole `test` folder
is a single test suite.

| Guide | What it covers |
| --- | --- |
| [Test hierarchy](./hierarchy.md) | Nesting test suites and selecting them per environment |
| [Shared code](./shared-code.md) | Sharing helpers between test suites and using the project's own code in tests |
| [Best practices](./best-practices.md) | Recommendations for maintainable tests |

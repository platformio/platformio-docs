<a id="check"></a>

# Static Code Analysis {#static-code-analysis}

**Automated code analysis without hassle!**

Static analysis became an important part of software development cycle. It can identify potential bugs, vulnerabilities and security threats by doing an analysis on the source code level without having to test it on hardware or execute any code.

**Static Code Analysis** helps reduce development cost by enabling engineers to detect the precise location of defects and eliminate issues more efficiently and earlier in the development cycle. It can also ensure compliance with internal or industry coding standards such as MISRA, CERT, etc.

**Key features**

- Fully integrated within the PlatformIO ecosystem and easy to execute on the entire project.
- Straightforward integration with [Continuous Integration](../ci/index.md) services.
- Possibility to reuse the same setup on other projects.
- Easy and flexible rule configuration.
- Comprehensive and detailed error information
- Multiple architectures and development platforms.
- Cross-platform: Windows, MacOS, Linux.

**Static Code Analysis** can detect a wide range of known defects in C/C++ code, including:

- Potential NULL pointer dereferences
- Possible indexing beyond array bounds
- Suspicious assignments
- Reads of potentially uninitialized objects
- Unused variables or functions
- Out of scope memory usage

:::warning

Before performing a static analysis check, make sure your project builds without errors. For information about how to build a project, see the [pio run](../../reference/cli/pio-run.md) command or [PlatformIO IDE for VSCode](../ide/vscode.md) guide.

:::

- [User Interface](./ui.md)

- [Defect severity](./severity.md)

- [Configuration](./configuration.md)

  - [Check options](../../reference/platformio-ini/env/check-options.md)

- [Check tools](./tools/index.md)

  - [Clang-Tidy](./tools/clang-tidy.md)
  - [Cppcheck](./tools/cppcheck.md)

- [CLI Guide](./cli.md)

  - [pio check](../../reference/cli/pio-check.md)

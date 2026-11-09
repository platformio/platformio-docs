---
description: Install or upgrade PlatformIO Core from PyPI with pip, for CI systems and containers.
---

# Install with pip

PlatformIO Core is published on [PyPI](https://pypi.org/project/platformio/).
Install it with [pip](https://pip.pypa.io) when you build in
[CI](../../guides/ci/index.md) or containers, or when you manage Python
environments yourself.

For a workstation, use the [installer script](./installer-script.md) instead:
it keeps PlatformIO in an isolated environment, so system Python upgrades
cannot break it.

To install or upgrade the latest stable version:

```bash
python3 -m pip install -U platformio
```

Install into a virtual environment rather than the system Python, so that
PlatformIO's dependencies do not conflict with other packages.

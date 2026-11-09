---
description: Build and test PlatformIO projects in GitHub Actions, GitLab CI, CircleCI and other continuous integration services.
---

# CI integrations

Build and test your project on every change with a
[continuous integration](https://en.wikipedia.org/wiki/Continuous_integration)
service, to catch errors early.

In CI, install PlatformIO Core [with pip](../../get-started/install/pip.md),
then run your usual commands:

- [`pio run`](../../reference/cli/pio-run.md) to build a PlatformIO project;
- [`pio test`](../../reference/cli/pio-test.md) to run
  [unit tests](../unit-testing/index.md), on the host or, through
  [remote development](../remote-development.md), on real hardware;
- [`pio check`](../../reference/cli/pio-check.md) for
  [static code analysis](../static-code-analysis/index.md);
- [`pio ci`](../../reference/cli/pio-ci.md) to build code that is not a
  PlatformIO project, such as library examples, for several boards.

To speed up builds, cache the `~/.platformio` folder and, optionally, the
project's `.pio` folder between runs.

## Services {#services}

| Service | |
| --- | --- |
| [GitHub Actions](./github-actions.md) | |
| [GitLab CI/CD](./gitlab.md) | |
| [CircleCI](./circleci.md) | |
| [Travis CI](./travis.md) | |
| [AppVeyor](./appveyor.md) | |
| [Drone](./drone.md) | |
| [Shippable](./shippable.md) | Discontinued; kept for reference |

Any other CI service works the same way: install Python and PlatformIO Core,
and run the commands above.

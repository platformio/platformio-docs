---
description: What a PlatformIO Account is for and how to manage it.
---

<a id="pioaccount"></a>

# PlatformIO Account {#platformio-account}

Building, uploading, debugging and testing firmware do not require an account.
You need a PlatformIO Account to:

- Post in the [Community forum](https://community.platformio.org/).
- Use [remote development](../guides/remote-development.md).
- [Publish packages](../reference/cli/pio-pkg/publish.md) to the PlatformIO
  Registry and [control who can access them](../reference/cli/pio-access/index.md).
- Manage [organizations](../reference/cli/pio-org/index.md) and
  [teams](../reference/cli/pio-team/index.md).

## Manage your account {#platformio-ide}

**In PlatformIO IDE**, open [PlatformIO Home](./platformio-home.md) and select
**Account**. There you can create an account, sign in (including with OAuth
providers), reset your password, update your profile and get an
authentication token. Signing in with OAuth is available only here.

<a id="cli-guide"></a>

**From the command line**, use [`pio account`](../reference/cli/pio-account/index.md):

| Command | What it does |
| --- | --- |
| [`pio account register`](../reference/cli/pio-account/register.md) | Create an account |
| [`pio account login`](../reference/cli/pio-account/login.md) | Sign in |
| [`pio account logout`](../reference/cli/pio-account/logout.md) | Sign out |
| [`pio account show`](../reference/cli/pio-account/show.md) | Show account details |
| [`pio account update`](../reference/cli/pio-account/update.md) | Update your profile |
| [`pio account password`](../reference/cli/pio-account/password.md) | Change your password |
| [`pio account forgot`](../reference/cli/pio-account/forgot.md) | Reset a forgotten password |
| [`pio account token`](../reference/cli/pio-account/token.md) | Get an authentication token, for example for CI |
| [`pio account destroy`](../reference/cli/pio-account/destroy.md) | Delete your account |

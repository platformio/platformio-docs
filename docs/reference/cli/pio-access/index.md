---
description: Manage who can access your packages in the PlatformIO Registry.
---

<a id="cmd-access"></a>

# pio access {#pio-access}

Manage access to resources (packages) you published in the
[PlatformIO Registry](https://registry.platformio.org): make them public or
private, and grant or revoke access for users and teams.

To change the access to a resource, you must:

- own the resource, or
- be a member of the team that owns it, or
- have `maintainer` access to it, directly or through a team.

Manage teams and their members with [`pio team`](../pio-team/index.md).

## Commands {#commands}

| Command | Description |
| --- | --- |
| [`pio access grant`](./grant.md) | Grant a user or a team access to a resource |
| [`pio access revoke`](./revoke.md) | Revoke a user's or a team's access to a resource |
| [`pio access list`](./list.md) | List the resources you can access |
| [`pio access public`](./public.md) | Make a resource public |
| [`pio access private`](./private.md) | Make a resource private |

For the options of a command, run `pio access COMMAND --help`.

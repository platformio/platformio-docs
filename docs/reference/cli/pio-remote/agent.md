<a id="cmd-remote-agent"></a>

# PlatformIO Remote Agent {#platformio-remote-agent}

Start [PlatformIO Remote Agent](#cmd-remote-agent) on a host machine and work remotely with your devices **WITHOUT** extra software, services, SSH, VPN, tunneling or opening incoming network ports.

[Remote Development](../../../guides/remote-development.md) supports wired and wireless devices. Wired devices should be connected physically to host machine where [PlatformIO Remote Agent](#cmd-remote-agent) is started, where wireless devices should be visible for [PlatformIO Remote Agent](#cmd-remote-agent) to provide network operations Over-The-Air (OTA).

<a id="cmd-remote-agent-list"></a>

## pio remote agent list {#pio-remote-agent-list}

### Usage {#usage}

```text
pio remote agent list
```

### Description {#description}

List active [PlatformIO Remote Agent](#cmd-remote-agent) s started using own [PlatformIO Account](../../../get-started/platformio-account.md) or shared with you by other PlatformIO developers.

### Example {#example}

```text
> pio remote agent list

innomac.local
-------------
ID: 98853d930......788d77375e7
Started: 2016-10-26 16:32:56
```

---

<a id="cmd-remote-agent-start"></a>

## pio remote agent start {#pio-remote-agent-start}

### Usage

```bash
pio remote agent start [OPTIONS]
```

### Description

Start [PlatformIO Remote Agent](#cmd-remote-agent) and work remotely with your devices from anywhere in the world. This command can be run as daemon or added to autostart list of your OS.

### Options {#options}

<a id="cmdoption-pio-remote-agent-start-name"></a>

#### `-n, --name` {#cmdoption-pio-remote-agent-start-n}

Agent name/alias. By default, machine's `hostname` will be used. You can use this name later for [pio remote device](./device.md) and [pio remote run](./run.md) commands. Good names are home, office, lab or etc.

<a id="cmdoption-pio-remote-agent-start-share"></a>

#### `-s, --share` {#cmdoption-pio-remote-agent-start-s}

Share your agent/devices with other PlatformIO developers who have [PlatformIO Account](../../../get-started/platformio-account.md): friends, co-workers, team, etc.

The valid value for `--share` option is email address that was used for [pio account register](../pio-account/register.md) command.

<a id="cmdoption-pio-remote-agent-start-working-dir"></a>

#### `-d, --working-dir` {#cmdoption-pio-remote-agent-start-d}

A working directory where [PlatformIO Remote Agent](#cmd-remote-agent) stores projects data for incremental synchronization and embedded programs for PlatformIO Process Supervisor.

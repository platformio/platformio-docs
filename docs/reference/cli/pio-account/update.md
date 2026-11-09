---
description: Update the profile of your PlatformIO Account.
---

# pio account update

Update the profile of your [PlatformIO Account](../../../get-started/platformio-account.md).

## Usage {#usage}

```bash
pio account update [OPTIONS]
```

## Description {#description}

Pass the fields to change as options. If you pass none, the command asks for
each field, with the current value as the default.

## Options {#options}

<a id="cmdoption-pio-account-register-current-password"></a>

### `--current-password` {#cmdoption-pio-account-update-current-password}

Your current password, to confirm the change. If you omit it, the command asks
for it.

<a id="cmdoption-pio-account-register-username"></a>

### `--username` {#cmdoption-pio-account-update-username}

A new username. Usernames can contain letters, digits and single hyphens, cannot begin or end
with a hyphen, and can be up to 38 characters long.

<a id="cmdoption-pio-account-register-email"></a>

### `--email` {#cmdoption-pio-account-update-email}

A new email address. PlatformIO sends a confirmation email to it.

<a id="cmdoption-pio-account-register-firstname"></a>

### `--firstname` {#cmdoption-pio-account-update-firstname}

A new first name.

<a id="cmdoption-pio-account-register-lastname"></a>

### `--lastname` {#cmdoption-pio-account-update-lastname}

A new last name.

# Asking for input (prompts)

Sometimes you need to ask the user for the input (Wi-Fi password, station name, etc). Python has a built-in [input()](https://docs.python.org/3/library/functions.html#input) function for this case.

See the example below on how to read a user name and set it to the `USER_NAME` macro.

`platformio.ini`:

```ini
[env:my_env]
platform = ...
extra_scripts = prompt-user-data.py
```

`prompt-user-data.py`:

```python
Import("env")

# Do not run a script when external applications, such as IDEs,
# dump integration data. Otherwise, input() will block the process
# waiting for the user input
if env.IsIntegrationDump():
    # stop the current script execution
    Return()

# Ask user name
print("Enter your name:")
user_name = input()
env.Append(
    CPPDEFINES=[("USER_NAME",  env.StringifyMacro(user_name))],
)
```

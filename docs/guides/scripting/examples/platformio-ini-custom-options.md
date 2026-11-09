# Custom options in `platformio.ini`

PlatformIO allows you extending project configuration with own data. Custom options have to start with `custom_` or `board_` to not generate a warning that the unknown configuration option will be ignored by PlatformIO. You can read these values later using [ProjectConfig API](https://github.com/platformio/platformio-core/blob/develop/platformio/project/config.py):

<dl>

<dt>

`ProjectConfig::get(section, option, default=None)`

</dt>

<dd>

Get an option value for the named section

</dd>

<dt>

`ProjectConfig::options(section)`

</dt>

<dd>

Returns a list of the sections available

</dd>

<dt>

`ProjectConfig::items(section, as_dict=False)`

</dt>

<dd>

Returns a list of "name", "value" pairs for the options in the given section or a dictionary when `as_dict=True` is passed

</dd>

<dt>

`ProjectConfig::has_section(section)`

</dt>

<dd>

Indicates whether the named section is present in the configuration

</dd>

<dt>

`ProjectConfig::has_option(section, option)`

</dt>

<dd>

If the given section exists, and contains the given option, returns `True`; otherwise returns `False`.

</dd>

</dl>

PlatformIO's "ProjectConfig" is compatible with a native Python's [ConfigParser](https://docs.python.org/3/library/configparser.html) API.

**Example**

`platformio.ini`:

```ini
[universe]
hello = world

[env:my_env]
platform = ...
extra_scripts = extra_script.py

custom_option1 = value1
custom_option2 = value2
```

`extra_script.py`:

```python
# "env.GetProjectOption" shortcut for the active environment
value1 = env.GetProjectOption("custom_option1")
value2 = env.GetProjectOption("custom_option2")

# Read value from other environments
config = env.GetProjectConfig()
world = config.get("universe", "hello")
```

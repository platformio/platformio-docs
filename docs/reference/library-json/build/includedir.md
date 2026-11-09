# `includeDir` {#includedir}

*Optional* | Type: `String`

The base path to be searched for header files. The default value is `include` and indicates that the folder is located at the root of the library. Setting `includeDir` to `.` will change the base path to the root of the library.

If you need to export additional relative paths, refer to [flags](./flags.md).

:::note

The [Library Dependency Finder (LDF)](../../../guides/libraries/ldf.md) will pick a library automatically only when a project or other dependent libraries include any header file located in `includeDir` or `srcDir`.

:::

**Example**

Override the base include path to the library root directory and provide the custom include paths:

```javascript
{
  "name": "SomeLib",
  "version": "0.0.0",
  "build": {
    "includeDir": ".",
    "flags": [
      "-I include",
      "-I extra",
      "-I drivers"
    ]
  }
}
```

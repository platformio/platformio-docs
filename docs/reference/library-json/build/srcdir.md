---
description: "The base path where PlatformIO should look for library source code."
---

# `srcDir`

- **Required:** No
- **Type:** String

The base path where PlatformIO should look for library source code. The default value is `src` and indicates that folder is located in the root of the library.

Setting `srcDir` to `.` will instruct PlatformIO to recursively build all source files located in the root of the library and its subfolders.

If you need to exclude some files from the build process, refer to the [srcFilter](./srcfilter.md).

## Example

Build ALL files starting from the root of a library and exclude `examples` and `test` subfolders:

```javascript
{
  "name": "SomeLib",
  "version": "0.0.0",
  "build": {
    "srcDir": ".",
    "srcFilter": "+<*> -<examples> -<test>"
  }
}
```

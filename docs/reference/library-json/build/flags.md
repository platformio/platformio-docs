<a id="library-json-buid-flags"></a>

# `flags` {#flags}

*Optional* | Type: `String` or `Array`

Extra flags to control preprocessing, compilation, assembly, and linking processes. More details [build_flags](../../platformio-ini/env/build-flags.md).

:::note

Keep in mind when operating with the `-I` flag (directories to be searched for header files). The path should be relative to the root directory where the `library.json` manifest is located.

:::

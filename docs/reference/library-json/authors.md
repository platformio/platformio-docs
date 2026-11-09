---
description: "An author contact information."
---

<a id="manifest-library-json-authors"></a>

# `authors` {#authors}

- **Required:** No
- **Type:** Object or array of objects

An author contact information

- `name` Full name (**Required**)
- `email`
- `url` An author's contact page
- `maintainer` Specify "maintainer" status

## Examples

```javascript
"authors":
{
    "name": "John Smith",
    "email": "me@john-smith.com",
    "url": "https://www.john-smith/contact"
}

...

"authors":
[
    {
        "name": "John Smith",
        "email": "me@john-smith.com",
        "url": "https://www.john-smith/contact"
    },
    {
        "name": "Andrew Smith",
        "email": "me@andrew-smith.com",
        "url": "https://www.andrew-smith/contact",
        "maintainer": true
    }
]
```

:::note

If [authors](#manifest-library-json-authors) field is not defined, PlatformIO will try to fetch data from VCS provider (Github, Gitlab, etc) if [repository](./repository.md) is declared.

:::

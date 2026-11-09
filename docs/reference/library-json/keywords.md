---
description: "Used for search by keyword."
---

# `keywords` {#keywords}

- **Required:** No (recommended for published packages)
- **Type:** String or array of strings
- **Limits:** Each keyword: at most 50 characters, only lowercase letters, digits, spaces and `+`, `_`, `-`, `.`.

Used for search by keyword. Helps to make your library easier to discover without people needing to know its name.

The keyword should be in lowercase and can consist of lowercase letters (a-z), digits, periods, underscores, plus symbols, and dashes. However, it should not start or end with a dot, underscore, plus symbol, or dash. You can provide a list of keywords by separating them with commas (`,`) or by declaring them as an array.

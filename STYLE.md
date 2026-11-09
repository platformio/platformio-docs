# PlatformIO Docs style guide

We follow the
[Google developer documentation style guide](https://developers.google.com/style).
This page lists the rules we apply most often and the ones specific to
PlatformIO. When in doubt, the Google guide wins.

## Audience

Embedded systems engineers and firmware developers. Assume they know C/C++,
microcontrollers and a terminal. Do not assume they know PlatformIO, Python or
SCons.

## Voice and tone

- Address the reader as **you**. Use the present tense and the active voice.
- Be direct and specific. Prefer "Run `pio run`" to "You may want to try
  running the `pio run` command".
- No marketing language: avoid "powerful", "next-generation", "unique",
  "seamless", "simply", "just", "easy". Describe what a feature does instead.
- Do not state numbers that age quickly (users, ratings, awards) unless the
  page is generated from data.

## Page types

| Type | Purpose | Shape |
| --- | --- | --- |
| Overview | What something is and when to use it | Short intro, key concepts, links onward |
| Tutorial | Learn by doing, end to end | Prerequisites, numbered steps, a working result, next steps |
| How-to guide | Solve one task | Goal, prerequisites, steps, result |
| Reference | Look up exact facts | Consistent structure per item; no narrative |

Start every page with one or two sentences saying what it covers and who it
is for.

## Headings

- Sentence case: "Install shell commands", not "Install Shell Commands".
- Use one `#` title per page; do not skip levels.
- Task headings start with a verb: "Install the udev rules".
- Keep existing explicit heading ids (`{#...}`) when you edit a heading, so
  links keep working. Add new ids only when another page links to the heading.

## Procedures

- Use numbered lists for steps that must happen in order; one action per step.
- Put the result or the expected output right after the step that produces it.
- Show commands in code blocks without a shell prompt (`$`, `>`), so they can
  be copied. Show output in a separate block labeled `text`.
- Mark placeholders as `<board_id>` and explain them.

## Formatting

- `Code font` for commands, options, file names, paths, environment
  variables, `platformio.ini` options and values.
- **Bold** only for UI labels ("Select **Open Project**"); not for emphasis.
- Admonitions: `:::note` for useful context, `:::tip` for optional shortcuts,
  `:::warning` for things that can break a build or a device, `:::danger` for
  data loss. Do not stack them; one per section at most.
- Tables for comparing options; lists for everything else.
- Link text describes the target ("see [Library Dependency Finder](...)"),
  never "click here".

## Terminology

Use the terms from PlatformIO Core's `GLOSSARY.md`. In particular:

| Use | Not |
| --- | --- |
| PlatformIO | Platformio, PIO (in prose) |
| PlatformIO Core | PIO Core, the core |
| PlatformIO IDE | PIO IDE |
| PlatformIO Home | PIO Home |
| `platformio.ini` | the ini file, project conf |
| development platform (or platform) | dev/platform |
| platform package (the installable package of a platform) | platform (when you mean the package) |
| project environment, `[env:NAME]` | working environment, env (in prose) |
| build configuration (`release`, `debug`, `test`) | build type, build mode |
| project target (`upload`, `clean`, ...) | target (when it could mean hardware) |
| target device (the physical hardware) | target, device (ambiguous) |
| board (a board definition), board ID | board identifier |
| package (installed by PlatformIO) vs library (source code) vs registry | interchangeably |
| Visual Studio Code (first use), VS Code | VSCode |

## Accuracy

Reference pages must match PlatformIO Core's source code: CLI commands in
`platformio/*/commands/`, `platformio.ini` options in
`platformio/project/options.py`, environment variables and settings in
`platformio/app.py`. When the docs and the code disagree, the docs follow the
code; list every such fix in the pull request description.

## Files

- Pages are Markdown (`.md`); use `.mdx` only when a page needs components.
- Kebab-case file names; the path is the URL.
- Images live in an `img/` folder next to the page that uses them.
- When you move or delete a page, add a redirect to `redirects.json`.

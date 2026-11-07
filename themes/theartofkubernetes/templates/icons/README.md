# Icons

Inner SVG markup of [Feather icons](https://feathericons.com) (MIT License, Copyright (c) 2013-2017 Cole Bemis).

Each file contains only the shapes (no outer `<svg>` tag). Render an icon with the
`icon()` macro from `partials/macros.html`, which wraps the shapes in a 24x24 stroked `<svg>`:

```jinja
{% from "partials/macros.html" import icon %}
{{ icon("book-open", "size-5 text-teal-600") }}
```

To add an icon, copy the inner markup of the Feather SVG into `<name>.svg`.

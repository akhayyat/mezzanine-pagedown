Mezzanine PageDown
==================

Inspired by [mezzanine-mdown][1], [django-pagedown][2], and
[django-markupmirror][3].

This package provides rich text widgets and filters for [Mezzanine][4]
to author content using Markdown syntax instead of the default TinyMCE
editor.


Features
--------

 - Uses the [PageDown][5] markdown editor from Stack Exchange
   (optional), and [Python-Markdown][6] for rendering.

 - Supports client-side and server-side live previews in the
   editor. Client-side previews use PageDown's JavaScript
   previewer. Server-side previews use the same rendering filter as
   the final page.

 - Supports bundled and custom [Python-Markdown extensions][7], and
   provides a few filters that are preconfigured to use some
   extensions, such as [Markdown Extra][8]. If server-side previews
   are enabled, configured extensions will be enabled in the editor
   preview.

 - HTML sanitizing using [Bleach][9]. Bleach is already a dependency
   of Mezzanine.

 - Integrates the editor's `Insert Image` button with Mezzanine's file
   browser (Media Library). Clicking the `Insert Image` button pops up
   an in-window selection dialog of Mezzanine's Media Library.


How to Use
----------

 1. Get and install the package:

        pip install mezzanine-pagedown

    Mezzanine 1.3 or higher is required.

 2. Install the app in your Mezzanine project by adding
    `mezzanine_pagedown` to the list of `INSTALLED_APPS` in your
    project's `settings.py`.

 3. Configure Mezzanine to use one of the provided rich text
    widgets. In your project's `settings.py`, set
    `RICHTEXT_WIDGET_CLASS` to:

     - `'mezzanine_pagedown.widgets.PageDownWidget'` to use the
       PageDown editor with live preview.

     - `'mezzanine_pagedown.widgets.PlainWidget'` to use a plain
       textarea without preview.

 4. Configure Mezzanine to use one of the provided rich text filters
    for rendering markdown content. In `settings.py`, set
    `RICHTEXT_FILTERS` to include one of the following:

     - `'mezzanine_pagedown.filters.plain'` to use plain Markdown
       syntax with no extensions.

     - `'mezzanine_pagedown.filters.extra'` to use Markdown Extra.

     - `'mezzanine_pagedown.filters.codehilite'` to enable the
       [CodeHilite][10] extension.

     - `'mezzanine_pagedown.filters.custom'` to enable an explicit
       list of extensions through the `PAGEDOWN_MARKDOWN_EXTENSIONS`
       setting (see below).

 5. Disable Mezzanine's HTML sanitizing so that it does not interfere
    with markdown's blockquote syntax (`>`):

        RICHTEXT_FILTER_LEVEL = 3

    mezzanine-pagedown provides its own sanitizing after rendering
    Markdown to HTML, and respects Mezzanine's
    `RICHTEXT_ALLOWED_TAGS`, `RICHTEXT_ALLOWED_ATTRIBUTES`, and
    `RICHTEXT_ALLOWED_STYLES` settings.

 6. (Optional): Server-side previews:

     - In `settings.py`, enable server-side live previews in the editor:

            PAGEDOWN_SERVER_SIDE_PREVIEW = True

        By default (`False`), previews are generated client-side using
        PageDown's previewer.

     - In `urls.py`, enable the preview URL:

            import mezzanine_pagedown.urls

        Then add the following line to `urlpatterns`:

            ("^pagedown/", include(mezzanine_pagedown.urls)),

        In this case, the preview URL is `/pagedown/preview/`. You can
        replace `"^pagedown/"` with your own path.

 7. (Optional): Set enabled extensions. Requires the `custom` filter:

        RICHTEXT_FILTERS = ['mezzanine_pagedown.filters.custom']
        PAGEDOWN_MARKDOWN_EXTENSIONS = ('extra','codehilite','toc')

    To use a [custom extension][11], import it and include an instance
    in the list of extensions:

        from myapp.markdown_extensions.myextension import MyExtension
        PAGEDOWN_MARKDOWN_EXTENSIONS = ('extra', MyExtension())

 8. (Optional): Generate and use a pygments CSS style for use with the
     CodeHilite extension (requires installing pygments):

        python manage.py pygments_styles <scheme_name>


License
-------

Licence: BSD. See included `LICENSE` file.

Note that this license applies to this repository only. The
[PageDown][5] JavaScript library is used as a sub-repository and has
its own license.


[1]: https://bitbucket.org/onelson/mezzanine-mdown
[2]: https://bitbucket.org/moberley/django-pagedown
[3]: https://bitbucket.org/fabianbuechler/django-markupmirror
[4]: http://mezzanine.jupo.org/
[5]: https://code.google.com/p/pagedown/ "Official PageDown project"
[6]: http://pythonhosted.org/Markdown/
[7]: http://pythonhosted.org/Markdown/extensions/index.html
[8]: http://pythonhosted.org/Markdown/extensions/extra.html
[9]: https://github.com/jsocol/bleach
[10]: http://packages.python.org/Markdown/extensions/code_hilite.html
[11]: http://pythonhosted.org/Markdown/extensions/api.html "Writing Extensions for Python-Markdown"

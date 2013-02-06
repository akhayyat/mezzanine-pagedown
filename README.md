Mezzanine PageDown
==================

Inspired by [mezzanine-mdown][1] and [django-pagedown][2].

This package provides widgets and filters for [Mezzanine][3] that
enable admins to use Markdown syntax to create their site content,
rather than using the TinyMCE editor to generate HTML code for rich
text content types, such as *rich text pages* and *blog posts*.


Differences
-----------

Differences between mezzanine-pagedown and:

 -  mezzanine-mdown: mezzanine-pagdown replaces OpenLibrary's wmd
    editor used by mezzanine-mdown with the [PageDown][4] JavaScript
    Markdown editor and previewer from Stack Exchange.

    PageDown have two main advantages over wmd:

     - Still maintained
     - Extensible via [hooks][5]

    Also, mezzanine-pagedown integrates with Mezzanine's file browser
    differently. See the differences between mezzanine-pagedown and
    django-pagedown below.

 -  django-pagedown: mezzanine-pagedown integrates the editor's `Insert
    Image` button with Mezzanine's file browser (Media
    Library). Clicking the `Insert Image` button pops up an in-window
    dialog of Mezzanine's Media Library.


Features
--------

### Widgets

mezzanine-pagedown provides two rich text widgets that can be used for
editing Mezzanine's rich text content fields:

 - `mezzanine_pagedown.widgets.PageDownWidget`: Uses the PageDown
   JavaScript editor and previewer.

 - `mezzanine_pagedown.widgets.PlainWidget`: Uses a plain text area.

### Filters

mezzanine-pagedown provides two rich text filters that can be used to
render Markdown content:

 - `mezzanine_pagedown.filters.codehilite`: Renders the content using
   Markdown with the [CodeHilite][6] extension enabled.

 - `mezzanine_pagedown.filters.plain`: Renders the content using
   vanilla Markdown formatting.

### CodeHilite Style Generation

mezzanine-pagedown shamelessly *reuses* (among other things)
[mezzanine-mdown][1]'s management command `pygments_styles`, which
allows you to generate CSS styles for colorizing code blocks parsed by
the CodeHilite filter.

This feature requires the `pygments` python package, which can be
installed by running:

    pip install pygments

Invoke the management command without arguments to see a usage message:

    $ python manage.py pygments_styles
    Usage: ./manage.py pygments_styles <scheme_name>
    Available color schemes:
      monokai
      manni
      rrt
      perldoc
      borland
      colorful
      default
      ...

Invoking with the scheme's name as an argument will print the CSS to
stdout:

    python manage.py pygment_styles colorful > pygments.css

In additon to this single scheme method, the command also accepts the
`--all` flag, which will generate styles for all available styles, but
with one key difference: each scheme is prefixed with its name as a
CSS class name. This is handy during theme development as you can
quickly switch pygments schemes just by setting the class on the body
tag to your choice of scheme without having to regenerate CSS files
constantly.


How to Use
----------

 1. Get and install the package:

        pip install mezzanine-pagedown

    Mezzanine 1.3 or higher is required.

 2. Install the app in your Mezzanine project by adding
    `mezzanine_pagedown` to the list of `INSTALLED_APPS` in your
    project's `settings.py`.

 3. Configure Mezzanine to use one of the provided widgets and filters
    for its rich text fields.

    In your project's `settings.py`, add the following two lines,
    depending on the widget and filter you would like to use:

     1. `RICHTEXT_WIDGET_CLASS = 'mezzanine_pagedown.widgets.PageDownWidget'`  
        Or:  
        `RICHTEXT_WIDGET_CLASS = 'mezzanine_pagedown.widgets.PlainWidget'`

     2. `RICHTEXT_FILTER = 'mezzanine_pagedown.filters.codehilite'`  
        Or:  
        `RICHTEXT_FILTER = 'mezzanine_pagedown.filters.plain'`

 4. (Optional): Generate and use a pygments CSS style:

        python manage.py pygments_styles <scheme_name>


License
-------

Licence: BSD. See included `LICENSE` file.

Note that this license applies to this repository only. The
[PageDown][4] JavaScript library is used as a sub-repository and has
its own license.


[1]: https://bitbucket.org/onelson/mezzanine-mdown
[2]: https://bitbucket.org/moberley/django-pagedown
[3]: http://mezzanine.jupo.org/
[4]: https://code.google.com/p/pagedown/ "Official PageDown project"
[5]: http://code.google.com/p/pagedown/wiki/PageDown#Plugin_hooks
[6]: http://packages.python.org/Markdown/extensions/code_hilite.html

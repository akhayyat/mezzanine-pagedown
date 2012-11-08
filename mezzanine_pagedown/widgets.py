from django import forms
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.forms.util import flatatt

from mezzanine.conf import settings

class PageDownWidget(forms.Textarea):
    """
    Widget providing Markdown preview using PageDown JavaScript
    """
    class Media:
        css = {'all': (
                'mezzanine_pagedown/css/pagedown.css',
                'mezzanine_pagedown/css/smoothness/jquery-ui-1.9.1.custom.min.css',)}
        js = ('mezzanine_pagedown/pagedown/Markdown.Converter.js',
              'mezzanine_pagedown/pagedown/Markdown.Sanitizer.js',
              'mezzanine_pagedown/pagedown/Markdown.Editor.js',
              'mezzanine/js/%s' % settings.JQUERY_FILENAME,
              'mezzanine_pagedown/js/jquery-ui-1.9.1.custom.min.js',
              'mezzanine_pagedown/js/pagedown.js',        )

    def __init__(self, template=None, *args, **kwargs):
        self.template = template or 'mezzanine_pagedown/editor.html'

        super(PageDownWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs={}):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_id = final_attrs['id']
        del final_attrs['id']
        return mark_safe(render_to_string(self.template, {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_unicode(value)),
            'id': final_id,
        }))

class PlainWidget(forms.Textarea):
    """
    A regular Textarea widget that is compatible with mezzanine richtext.
    """

    class Media:
        pass
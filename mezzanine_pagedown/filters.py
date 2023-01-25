from mezzanine.conf import settings

from markdown import markdown
from bleach import clean
try:
    from bleach.css_sanitizer import CSSSanitizer
except ImportError:
    CSSSanitizer = None


def _clean(html):
    tags = settings.RICHTEXT_ALLOWED_TAGS
    attrs = list(settings.RICHTEXT_ALLOWED_ATTRIBUTES)
    if CSSSanitizer is not None:
        # Bleach 5
        styles_options = {'css_sanitizer': CSSSanitizer(
            allowed_css_properties=settings.RICHTEXT_ALLOWED_STYLES
        )}
    else:
        styles_options = {'styles': settings.RICHTEXT_ALLOWED_STYLES}
    return clean(html, tags=tags, attributes=attrs, strip=True,
                 strip_comments=False, **styles_options)


def codehilite(content):
    """
    Renders content using markdown with the codehilite extension.
    """
    return _clean(markdown(content, ['codehilite',]))


def plain(content):
    """
    Renders content using markdown (no extensions).
    """
    return _clean(markdown(content))


def extra(content):
    """
    Renders content using markdown extra.
    """
    return _clean(markdown(content, ['extra',]))


def custom(content):
    """
    Renders content using markdown with the extensions listed in
    ``settings.PAGEDOWN_MARKDOWN_EXTENSIONS``.
    """
    return _clean(markdown(content,
            extensions=settings.PAGEDOWN_MARKDOWN_EXTENSIONS))

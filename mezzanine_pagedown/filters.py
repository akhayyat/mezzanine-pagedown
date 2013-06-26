from mezzanine.conf import settings

from markdown import markdown
from bleach import clean


def _clean(html):
    tags = settings.RICHTEXT_ALLOWED_TAGS
    attrs = settings.RICHTEXT_ALLOWED_ATTRIBUTES
    styles = settings.RICHTEXT_ALLOWED_STYLES
    return clean(html, tags=tags, attributes=attrs, strip=True,
                 strip_comments=False, styles=styles)


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

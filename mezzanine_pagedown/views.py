from django.http import HttpResponse
from django.views.generic import View

from mezzanine.conf import settings
from mezzanine.utils.importing import import_dotted_path


render = import_dotted_path(settings.RICHTEXT_FILTER)


class MarkupPreview(View):
    """
    Renders markdown content to HTML for preview purposes.
    """

    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        text = self.request.POST.get('text', u"")
        return HttpResponse(render(text), content_type='text/html')

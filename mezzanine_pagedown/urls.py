from django.conf.urls import patterns, url

from .views import MarkupPreview

urlpatterns = patterns('',
    url(r'^preview/$', MarkupPreview.as_view(), name='preview'),
)

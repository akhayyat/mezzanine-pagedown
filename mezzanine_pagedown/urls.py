from django.conf.urls import url

from .views import MarkupPreview

urlpatterns = [url(r'^preview/$', MarkupPreview.as_view(), name='preview'), ]

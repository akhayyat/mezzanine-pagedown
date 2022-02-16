from django.urls import path

from .views import MarkupPreview

urlpatterns = [path('preview/', MarkupPreview.as_view(), name='preview'), ]

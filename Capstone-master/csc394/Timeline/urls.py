# Timeline url patterns

from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.timeline_index, name='timeline_index'),
]

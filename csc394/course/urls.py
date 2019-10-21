from django.urls import path, re_path
from . import views

urlpatterns = [
    #/course/
    path('', views.index, name = 'index'),

    #/course/courseNum
    re_path(r'(?P<projId>[0-9]+)/$', views.coursePg, name = 'coursePg'),
]

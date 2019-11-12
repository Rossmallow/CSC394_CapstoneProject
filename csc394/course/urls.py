from django.urls import path, re_path
from . import views

urlpatterns = [
    #/course/
    path('', views.index, name = 'index'),
    #/course/courseNum
    path('<int:courseId>/', views.coursePg, name = 'coursePg'),
    path('<int:courseId>/<int:projId>/', views.projPg, name = 'projPg')
    #re_path(r'(?P<projId>[0-9]+)/$', views.projPg, name = 'projPg')
]
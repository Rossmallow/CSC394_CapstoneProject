from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
   path('', views.login_index, name='login_index'),
   url('register',views.UserFormView.as_view(), name='register'),
 ]
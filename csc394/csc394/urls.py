"""csc394 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from tasks.views import taskView, addTodo, deleteTodo, testTaskView

=======
from tasks.views import taskView, addTodo, deleteTodo, details
>>>>>>> 737476c08d98195d3cc6f45774aa5ad4e23a7e51


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('timeline/', include('Timeline.urls')),
<<<<<<< HEAD
    path('tasks/', taskView, name="tasksPage"),
=======
    path('tasks/', taskView),
    path('tasks/<int:todo_id>/',details),
>>>>>>> 737476c08d98195d3cc6f45774aa5ad4e23a7e51
    path('addTodo/', addTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('testTaskView/', testTaskView),
   
]

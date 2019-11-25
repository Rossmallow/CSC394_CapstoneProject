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
from tasks.views import taskView, addTodo, editTodo, deleteTodo, todoDetails, formView, changeStatus, addComment, editComment, deleteComment
from django.conf import settings
from django.conf.urls.static import static
=======
from tasks.views import taskView, addTodo, editTodo, deleteTodo, todoDetails, addComment, editComment, deleteComment
from reviews.views import addReview
>>>>>>> e887e5c1de2e0e5149998c2358f1320fb07bd452


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('login.urls')),
    path('timeline/', include('Timeline.urls')),
    path('tasks/', taskView),
    path('addTodo/', addTodo),
    path('editTodo/<int:todo_id>/', editTodo),
    path('deleteTodo/<int:todo_id>/', deleteTodo),
    path('tasks/<int:todo_id>/', todoDetails),
<<<<<<< HEAD
    path('reviews/',include('reviews.urls')),
    path('formView/', formView),
    path('changeStatus/<int:todo_id>/', changeStatus),
=======
    path('reviews/', include('reviews.urls')),
    path('addReview/', addReview),
>>>>>>> e887e5c1de2e0e5149998c2358f1320fb07bd452
    path('chat/', include('chat.urls')),
    path('tasks/<int:todo_id>/addComment/', addComment),
    path('tasks/<int:todo_id>/editComment/<int:comment_id>/', editComment),
    path('tasks/<int:todo_id>/deleteComment/<int:comment_id>/', deleteComment)
]

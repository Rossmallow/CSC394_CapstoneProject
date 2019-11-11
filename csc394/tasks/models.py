from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone




# Create your models here.
# class TodoList(models.Model):
#     user = models.ForeignKey(User)
#     name = models.TextField()


class TodoItem(models.Model):
    # todolist = models.ForeignKey('TodoList', on_delete=models.CASCADE)
    content = models.TextField()
    title = models.TextField(default='')
    date = models.DateField(auto_now=True)
    
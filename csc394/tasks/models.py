from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    title = models.TextField(default='')
    date = models.DateField(default='1999-01-13')
    user = models.TextField(default='Self')
    status = models.TextField(default='inProgress')

    def __str__(self):
        return self.title + '-' + self.user

class Comment(models.Model):
    todoItem = models.ForeignKey(TodoItem, on_delete=models.CASCADE)
    title = models.TextField(default='')
    body = models.TextField(default='')
    user = models.TextField(default='')

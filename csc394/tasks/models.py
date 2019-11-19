from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    title = models.TextField(default='')
    date = models.DateField(auto_now_add=False, auto_now=False)
    user = models.TextField(default='Self')
    status = models.TextField(default="todo")

    def __str__(self):
        return self.title + '-' + self.user
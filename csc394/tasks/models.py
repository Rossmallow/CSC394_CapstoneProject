from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.TextField()
    title = models.TextField(default='')
    date = models.DateField(default='1999-01-13')
    user = models.TextField(default='Self')

    def __str__(self):
        return self.title + '-' + self.user
sfrom django.db import models
from tasks.models import TodoItem
from django.contrib.auth.models import User

# Create your models here.

class newsItem(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default= True)
    subject = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = models.TextField(blank =False, null=True )
    relatedItem = models.ForeignKey(TodoItem, blank=True, null=True,on_delete=models.SET_NULL)
    #viewed = models.BooleanField(default = False)
    def __str__(self):
        return self.subject

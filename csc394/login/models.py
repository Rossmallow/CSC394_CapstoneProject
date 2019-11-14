from django.db import models
from tasks.models import TodoItem
# Create your models here.

class Course(models.Model):
    courseNum = models.IntegerField()
    title = models.CharField(max_length = 100,default = 'nullCourse')
    instructor = models.CharField(max_length = 250)
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return str(self.courseNum) + ' - ' + self.title
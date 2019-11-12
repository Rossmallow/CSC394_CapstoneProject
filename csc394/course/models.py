from django.db import models
from login.models import Course

class enrolledStud(models.Model):
    courseId = models.ForeignKey('login.Course', on_delete = models.CASCADE)
    studentId = models.IntegerField()
    firstName = models.CharField(max_length = 250)
    lastName = models.CharField(max_length = 250)
    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Project(models.Model):
    courseId = models.ForeignKey('login.Course', on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    members = models.ManyToManyField(enrolledStud)
    startDate = models.DateField()
    endDate = models.DateField()
    def __str__(self):
        return self.title
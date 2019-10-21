from django.db import models


class Course(models.Model):
    courseNum = models.IntegerField()
    title = models.CharField(max_length = 100,default = 'nullCourse')
    instructor = models.CharField(max_length = 250)
    maxEnrollment = models.IntegerField()
    startDate = models.DateField()
    endDate = models.DateField()

    def __str__(self):
        return str(self.courseNum) + ' - ' + self.title

#class enrolledStud(models.Modle):
 
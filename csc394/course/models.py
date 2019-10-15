from django.db import models


class Course(models.Modle):
    courseNum = models.IntegerField()
    instructor = models.CharFirld(max_length = 250)
    maxEnrollment = modles.IntegerFiled()
    startData = modles.DataField()
    endDate = models.DateField()

class enrolledStud(models.Modle):
 
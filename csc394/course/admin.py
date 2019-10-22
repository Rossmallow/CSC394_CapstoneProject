from django.contrib import admin
from .models import Course, Project, enrolledStud
# Register your models here.
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(enrolledStud)
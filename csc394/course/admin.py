from django.contrib import admin
from .models import Project, enrolledStud

# Register your models here.
admin.site.register(Project)
admin.site.register(enrolledStud)
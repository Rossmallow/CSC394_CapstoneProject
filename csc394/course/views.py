from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course, Project


def index(request):
    allProj = Project.objects.all()
    template = loader.get_template('course/index.html')
    context = {
        'course' : Course.objects.first(),
        'allProj' : allProj,
    }
    return HttpResponse(template.render(context, request))



def projPg(request, projId):
    #template = loader.get_template('course/projPg.html')
    return  HttpResponse("<h2>Projects for course " + str(projId) +"<h2>")


# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import enrolledStud, Project
from login.models import Course


def index(request):
    #return  HttpResponse("<h2>Projects for course <h2>")
    context = {
        'allCourse' : Course.objects.all(),
    }
    return render(request, 'course/index.html',context)

def coursePg(request, courseId):
    context = {
        'course' : Course.objects.get(pk = courseId),
        'allProj' : Project.objects.filter(courseId = courseId)
    }
    return render(request, 'course/coursePg.html',context)

def projPg(request, courseId, projId):
    try: 
        proj = Project.objects.get(pk = projId)
        context = {'proj' : proj}
    except Project.DoesNotExist:
        raise Http404('Not valid project')
    return  render(request, 'course/projPg.html', context)
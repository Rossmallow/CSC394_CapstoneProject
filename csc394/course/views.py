from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Course, Project


def index(request):
    allProj = Project.objects.all()
    #template = loader.get_template('course/index.html')
    context = {
        'course' : Course.objects.first(),
        'allProj' : allProj,
    }
    return render(request, 'course/index.html',context)



def projPg(request, projId):
    try: 
        proj = Project.objects.get(pk = projId)
        context = {'proj' : proj}
    except Project.DoesNotExist:
        raise Http404('Not valid project')
    #return  HttpResponse("<h2>Projects for course " + str(projId) +"<h2>")
    return  render(request, 'course/projPg.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

def index(request):
    allCourses = Course.objects.all()
    html = ''
    html += "<h1>Course Home Page <h1> "
    for proj in allCourses:
        url = 'course/'+str(proj.id)+'/'
        html +='<a href="'+ url+ '">'+ proj.title +'/a><br>'
    return HttpResponse(html)



def coursePg(request, projId):
   return  HttpResponse("<h2>Projects for course " + str(projId) +"<h2>")

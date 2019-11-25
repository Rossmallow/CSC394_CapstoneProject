from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Review

# Create your views here.


def index(request):
    return render(request, 'reviews/newReview.html')


def addReview(request):
    newReview = Review(name=request.POST['task'], performance=request.POST['performance'],
                       improvement=request.POST['improvement'], additionalInfo=request.POST['additionalInfo'])
    newReview.save()
    return HttpResponseRedirect('/reviews/')

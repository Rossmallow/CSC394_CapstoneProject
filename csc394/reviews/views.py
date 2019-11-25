from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Review
from tasks.models import TodoItem

# Create your views here.


def index(request, todo_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    try:
        todoItem = TodoItem.objects.get(pk=todo_id)
    except TodoItem.DoesNotExist:
        return HttpResponse("Task does not exist and cannot be reviewed", status=404)

    return render(request, 'reviews/newReview.html', {'todoItem': todoItem})


def addReview(request):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    newReview = Review(name=request.POST['task'], performance=request.POST['performance'],
                       improvement=request.POST['improvement'], additionalInfo=request.POST['additionalInfo'])
    newReview.save()
    return HttpResponseRedirect('/tasks/')

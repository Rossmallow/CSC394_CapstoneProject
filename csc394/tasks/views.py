from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def taskView (request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'tasks.html',
    {'all_items': all_todo_items})

def addTodo(request):
    new_item = TodoItem(content = request.POST['content'], title = request.POST['title'], date= request.POST['date'])
    new_item.save()
    return HttpResponseRedirect('/tasks/')
    #create new todo all_items
    
def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks/')
    #create new todo all_items

def taskDescription()
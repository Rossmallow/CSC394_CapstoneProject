from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, Comment

# Create your views here.


def taskView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'tasks.html',
                  {'all_items': all_todo_items})


def addTodo(request):
    new_item = TodoItem(
        content=request.POST['content'], title=request.POST['title'],
        date=request.POST['date'], user=request.POST['user'], status=request.POST['inProgress'])
    new_item.save()
    return HttpResponseRedirect('/tasks/')
    # create new todo all_items


def editTodo(request, todo_id):
    item_to_edit = TodoItem.objects.get(id=todo_id)
    item_to_edit.content = request.POST['content']
    item_to_edit.title = request.POST['title']
    item_to_edit.date = request.POST['date']
    item_to_edit.user = request.POST['user']
    item_to_edit.save()
    return HttpResponseRedirect('/tasks/{0}'.format(todo_id))


def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks/')
    # create new todo all_items


def todoDetails(request, todo_id):
    try:
        todoItem = TodoItem.objects.get(pk=todo_id)
    except TodoItem.DoesNotExist:
        return HttpResponse("Task does not exist", status=404)
    return render(request, 'tasks/taskDetails.html', {'todoItem': todoItem})

def addComment(request, todo_id):
    new_item = Comment(
        todoItem=request.POST['todoItem'], title=request.POST['title'], 
        body=request.POST['body'], user=request.POST['user'])
    new_item.save()
    return HttpResponseRedirect('/tasks/{0}'.format(todo_id))
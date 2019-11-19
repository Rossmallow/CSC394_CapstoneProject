from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem, Comment
from django.contrib.auth import authenticate

# Create your views here.


def taskView(request):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    all_todo_items = TodoItem.objects.all()
    return render(request, 'tasks.html',
                  {'all_items': all_todo_items})


def addTodo(request):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    new_item = TodoItem(
        content=request.POST['content'], title=request.POST['title'],
        date=request.POST['date'], user=request.POST['user'], status='inProgress')
    new_item.save()
    return HttpResponseRedirect('/tasks/')
    # create new todo all_items


def editTodo(request, todo_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    item_to_edit = TodoItem.objects.get(id=todo_id)
    item_to_edit.content = request.POST['content']
    item_to_edit.title = request.POST['title']
    item_to_edit.date = request.POST['date']
    item_to_edit.user = request.POST['user']
    item_to_edit.save()
    return HttpResponseRedirect('/tasks/{0}'.format(todo_id))


def deleteTodo(request, todo_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks/')
    # create new todo all_items


def todoDetails(request, todo_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    try:
        todoItem = TodoItem.objects.get(pk=todo_id)
    except TodoItem.DoesNotExist:
        return HttpResponse("Task does not exist", status=404)
    comments = Comment.objects.filter(todoItem=todo_id)
    return render(request, 'tasks/taskDetails.html', {'todoItem': todoItem, 'comments': comments})

def addComment(request, todo_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    new_item = Comment(
        todoItem=TodoItem.objects.get(id = request.POST['todoItem']), 
        title=request.POST['title'], body=request.POST['body'], 
        user=request.POST['user'])
    new_item.save()
    return HttpResponseRedirect('/tasks/{0}'.format(todo_id))

def deleteComment(request, todo_id, comment_id):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')

    item_to_delete = Comment.objects.get(pk=comment_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/tasks/{0}'.format(todo_id))
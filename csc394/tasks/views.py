from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoItem
from .forms import TodoForm

# Create your views here.
def formView(request):
    form = TodoForm()
    return render(request, 'formview.html', {'form': form})

def taskView(request):
    todo_items = TodoItem.objects.filter(status="todo")
    todo_inProgress = TodoItem.objects.filter(status="inProgress")
    todo_completed = TodoItem.objects.filter(status="completed")

    return render(request, 'tasks.html',
                  {'todo': todo_items, 'inProgress': todo_inProgress, 'completed': todo_completed})


def addTodo(request):
    new_item = TodoItem(
        content=request.POST['content'], title=request.POST['title'],
        date=request.POST['date'], user=request.POST['user'])
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
    return HttpResponseRedirect('/tasks/{}'.format(todo_id))


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

def completeTodo(request, todo_id):
    completedItem = TodoItem.objects.get(id=todo_id)
    completedItem.complete = true
    completedItem.save()
    return HttpResponseRedirect('/tasks/')

def changeStatus(request, todo_id):
    todo_itemStatus = TodoItem.objects.get(id=todo_id)
    todo_itemStatus.status = request.POST['status']
    todo_itemStatus.save()
    return HttpResponseRedirect('/tasks/')
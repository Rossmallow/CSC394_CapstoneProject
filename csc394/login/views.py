from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.contrib.auth import logout
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from tasks.views import taskView
from tasks.models import TodoItem
# Create your views here.

def login_index(request):

    return render(request, 'login/index.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/dashboard.html')
            else:
                return render(request, 'login/signin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login/signin.html', {'error_message': 'Invalid login'})
    return render(request, 'login/signin.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'login/signin.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'login/dashboard.html')
    context = {
        "form": form,
    }
    return render(request, 'login/registration.html', context)
   
def dashboard(request):
    if not request.user.is_authenticated:
        return render(request, 'login/signin.html')
    queryset = TodoItem.objects.all()
    context = {
        "object_list":queryset
        }
    return render(request,'login/dashboard.html')
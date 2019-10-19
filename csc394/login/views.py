from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login 
from django.views import generic
from django.views.generic import View
from .forms import UserForm
# Create your views here.

def login_index(request):

    return HttpResponse("<h1>Login Homepage</h1>")

class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration.html'
    
    #display blank html form

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})
 
    #process form data into datbase

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            #get clean data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user is not None:

                if user.is_active:
                    login(request,user)
                    return redirect ('login_index')
        return render(request, self.template_name, {'form':form})
   
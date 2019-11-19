from django.contrib.auth.models import User
from django import forms
from .models import newsItem
from django.views.generic import CreateView


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class newsForm(forms.ModelForm):
    class Meta:
        model = newsItem
        fields = ['subject', 'body','relatedItem',]
        exclude = ['creator']

    def form_valid(self,form):
        form.instance.creator = self.request.user
        return super().form_valid(form)



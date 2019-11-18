from django.contrib.auth.models import User
from django import forms
from .models import newsItem

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

class newsForm(forms.ModelForm):
    class Meta:
        model = newsItem
        fields = ['subject', 'body']


from django import forms

# class DateInput(forms.DateInput):
#     input_type = 'date'

class TodoForm(forms.Form):
    content = forms.CharField(label='Description',widget=forms.Textarea)
    title = forms.CharField(label='Title', max_length=100)
    date = forms.DateField(label='Date')
    user = forms.CharField(label='User',max_length=100)
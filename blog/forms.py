from django import forms
from django.forms import ModelForm, widgets
from . import models

class PostForm(ModelForm):
    class Meta:
        model = models.contact
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs = {'class':'field', 'style':'margin-bottom: 20px;'}),
            'email' : forms.EmailInput(attrs = {'class':'field', 'style':'margin-bottom: 20px;'}),
            'message' : forms.Textarea(attrs = {'class':'field', 'style':'margin-bottom: 20px;', 'rows':3})
        }
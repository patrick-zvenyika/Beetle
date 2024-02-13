from django import forms
from django.db import models
from .models import Post, Response


class NewPostForm(forms.ModelForm):
   
    class Meta:
         model = Post
         fields = ['title','subject','body','file']

         widgets ={
             'title':forms.TextInput(attrs={
                 'autofocus' : True,
                'placeholder' : 'Your question title',
                })
         }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body','file']
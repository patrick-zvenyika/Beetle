from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Post, Response

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class meta:
        model = User
        fields = ['username','email','password1','password2']


    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs ={'placeholder' : '@jandoe'}
        self.fields['email'].widget.attrs ={'placeholder' : 'jandoe@gmail.com'}
        self.fields['password1'].widget.attrs ={'placeholder' : 'Password'}
        self.fields['password2'].widget.attrs ={'placeholder' : 'Confirm Password'}

class LoginForm(AuthenticationForm):
    class meta:
        fields : '__all__'

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs ={'placeholder':'@jandoe'}
        self.fields['password'].widget.attrs ={'placeholder': 'Password'}

class NewPostForm(forms.ModelForm):

    class Meta:
         model = Post
         fields = ['title','subject','body','file']

         widgets ={
             'title':forms.TextInput(attrs={
                 'autofocus' : True,
                'placeholder' : 'Your question title',
                'class': 'form-control'
                }),
                'subject':forms.TextInput(attrs={
                 'autofocus' : True,
                'placeholder' : 'Tag/Subject',
                'class': 'form-control'
                }),
                'body':forms.Textarea(attrs={
                 'autofocus' : True,
                'placeholder' : 'Your post content',
                'style': 'height: 100px; width: 320px; resize: none;  background-color: hsl(218, 23%, 23%); color: white; border-radius: 3px; padding: 0 10px; margin-top: 8px; font-size: 14px; font-weight: 300; margin-bottom: 40px;',
                'class': 'form-control'
                }),
                'file':forms.FileInput(attrs={
                 'autofocus' : True,
                'class': 'form-control',
                'style': 'height: 50px; width: 325px;',
                }),
         }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body','file']

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from .models import Question, Response

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

class NewQuestionForm(forms.ModelForm):

    class Meta:
         model = Question
         fields = ['title','subject','body']

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

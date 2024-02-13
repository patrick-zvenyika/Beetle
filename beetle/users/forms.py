from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class meta:
        model = User
        fields = ['username','email','password1','password2']
        

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs ={'class':'form-control','placeholder' : 'Username'}
        self.fields['email'].widget.attrs ={'placeholder' : 'Email'}
        self.fields['password1'].widget.attrs ={'placeholder' : 'Password'}
        self.fields['password2'].widget.attrs ={'placeholder' : 'Confirm Password'}

class LoginForm(AuthenticationForm):
    class meta:
        fields : '__all__'
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs ={'placeholder':'Username'}
        self.fields['password'].widget.attrs ={'placeholder': 'Password'}
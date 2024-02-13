from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def registerPage(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        try:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                messages.success(request, "Account successfully created!")
                login(request, user)
                return redirect('login') 
        except Exception as e:
            print(e)
            raise

    context = {
        'form': form
        
    }
    return render(request, 'auth/signup.html', context)


def loginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        try:
            form = LoginForm(data = request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('home') 
        except Exception as e:
            print(e)
            raise

    context = {'form':form}
    return render(request, 'auth/signin.html', context)
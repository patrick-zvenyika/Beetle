from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Post, Response
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
# Create your views here.
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exit!')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Username Or Password does not exist!')

    return render(request, 'auth/login.html')


def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            # Check if passwords match
            if password1 != password2:
                messages.error(request,"Passwords do not match")

            # Check if username is already taken
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")

            # Check if email is already taken
            if User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password1)

            # Redirect to login page after successful registration
            return redirect('login')
        except ValueError as e:
            # Handle registration errors
            messages.error(request, str(e))
        except Exception as e:
            # Handle other exceptions
            messages.error(request, str(e))

    # Render registration page
    return render(request, 'auth/register.html')

def Logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url = 'login')
def main(request):
    # questions = Question.objects.all().order_by('-created_at')
    # context = {
    #     'questions' : questions
    # }
    return render (request, 'dashboard/index.html')

@login_required(login_url = 'login')
def CreatePost(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            file = form.cleaned_data['file']

            messages.success(request, 'Post created successfully!')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}:{error}")
    
    else:
        form = NewPostForm()

    return render (request, 'dashboard/new-post.html', {'form':form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from django.contrib import messages
from .forms import *
# Create your views here.
def loginPage(request):
    return render(request, 'auth/signup.html')

def registerPage(request):
    return render(request, 'auth/index.html')

#@login_required(login_url = 'login.html')
def main(request):
    # questions = Question.objects.all().order_by('-created_at')
    # context = {
    #     'questions' : questions
    # }
    return render (request, 'dashboard/index.html')

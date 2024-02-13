from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Response, Post
from django.contrib import messages
from .forms import *
# Create your views here.
def main(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts' : posts
    }
    return render (request, 'dashboard/index.html', context)


def newPostPage(request):
    form = NewPostForm()

    if request.method == 'POST':
        try:
            form = NewPostForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES.get('file')
                post = form.save(commit=False)
                post.author = request.user
                post.save()
        except Exception as e:
            print(e)
            raise
    context = {'form': form
    }
    return render(request, 'dashboard/new-post.html', context)


def responsePage(request, id):
    response_form = NewResponseForm()

    if request.method == 'POST':
        
        try:
            response_form = NewResponseForm(request.POST, request.FILES)

            if response_form.is_valid():
                file = request.FILES.get('file')
                response = response_form.save(commit = False)
                response.user = request.user
                response.question = Question(id = id)
                response.save()
                messages.success(request, 'Response submitted!')
                return redirect('/question/'+str(id)+'#'+str(response.id))
            elif response_form.is_valid():
                response = response_form.save(commit = False)
                response.user = request.user
                response.question = Question(id = id)
                response.save()
                messages.success(request, 'Response submitted!')
                return redirect('/question/'+str(id)+'#'+str(response.id))
           
        except Exception as e:
            print(e)
            raise
        


    question = Question.objects.get(id = id)
    context = {
        'question' : question,
        'response_form' : response_form
    }
    return render(request, 'dashboard/post-detail.html', context)


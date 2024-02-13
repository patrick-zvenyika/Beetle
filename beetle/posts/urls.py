from django.urls import path
from .views import *

urlpatterns = [
    path('blog-feeds/', main, name='feed'),
    path('blog-new-post/', newPostPage, name='new-post'),
    path('blog-post-view/', responsePage, name='new-response'),
]

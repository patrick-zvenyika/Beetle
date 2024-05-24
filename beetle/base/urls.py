from django.urls import path
from .views import *
urlpatterns = [
    path('', loginPage, name='login'),
    path('/register/', registerPage, name='register'),
    path('/logout/', Logout, name='logout'),
    path('dashboard/', main, name='home'),
    path('dashboard/file/<int:pk>/', download_file, name='item_download'),
    path('create_post/', CreatePost, name='create_post'),
 ]

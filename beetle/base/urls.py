from django.urls import path
from .views import *
urlpatterns = [
    path('', loginPage, name='login'),
    path('/register/', registerPage, name='register'),
    path('/dashboard/', main, name='home')
 ]

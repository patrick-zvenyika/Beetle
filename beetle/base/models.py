from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length = 30)

    def __str__(self):
        return self.subject

class Post(models.Model):
    author = models.ForeignKey(User, null=True, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300,null=False)
    subject = models.ForeignKey(Subject,null=True, on_delete = models.CASCADE)
    body = models.TextField(null=True)
    file = models.FileField( upload_to='media',blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title

    def get_responses(self):
        return self.responses.filter(parent=None)

class Response(models.Model):
    user = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    question = models.ForeignKey(Post, null=False, on_delete = models.CASCADE, related_name = 'responses')
    parent = models.ForeignKey('self', null=True, blank = True, on_delete = models.CASCADE)
    body = models.TextField(null = False)
    file = models.FileField( upload_to='media',blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Response.object.filter(parent=self)

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return HttpResponse(posts)
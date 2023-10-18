from django.shortcuts import render
from .models import BlogPost
# Create your views here.


def index(request):
    blog_post = BlogPost.objects.all()
    return render(request,"index.html",{"posts":blog_post})
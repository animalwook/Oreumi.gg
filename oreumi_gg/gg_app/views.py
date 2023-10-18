from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def index(request):
    return render(request, "oreumi_gg/index.html")

def champions(request):
    return render(request, "oreumi_gg/champions.html")

def community(request):
    blog_post = BlogPost.objects.all()
    return render(request,"oreumi_gg/community.html",{"posts":blog_post})

def login(request):
    return render(request, "oreumi_gg/login.html")

def register(request):
    return render(request, "oreumi_gg/register.html")




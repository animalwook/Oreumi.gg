from django.shortcuts import render,redirect
from .models import BlogPost
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import SignUpForm
# Create your views here.

def index(request):
    return render(request, "oreumi_gg/index.html")

def champions(request):
    return render(request, "oreumi_gg/champions.html")

def community(request):
    blog_post = BlogPost.objects.all()
    return render(request,"oreumi_gg/community.html",{"posts":blog_post})

def custom_login(request):
    if request.method == "GET":
        return render(request, 'registration/login.html')
    
    elif request.method == "POST":
        user = request.POST['username']
        pw = request.POST['password']
        check = authenticate(request, username=user, password=pw)
        if check is not None :
            login(request, check)
            return redirect('gg_app:index')
        else: return render(request, "registration/login.html")


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('gg_app:index')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import BlogPost
# Create your views here.

def index(request):
    return render(request, "oreumi_gg/index.html")

def champions(request):
    return render(request, "oreumi_gg/champions.html")

def leaderboards(request):
    return render(request, "oreumi_gg/leaderboards/leaderboards.html")

def type_champions(request):
    return render(request, "oreumi_gg/leaderboards/type_champions.html")

def type_ladder_flex (request):
    return render(request, "oreumi_gg/leaderboards/type_ladder_flex.html")

def type_ladder(request):
    return render(request, "oreumi_gg/leaderboards/type_ladder.html")

def type_level(request):
    return render(request, "oreumi_gg/leaderboards/type_level.html")

def community(request):
    blog_post = BlogPost.objects.all()
    return render(request,"community/community.html",{"posts":blog_post})

def login(request):
    return render(request, "registration/login.html")

def register(request):
    return render(request, "registration/register.html")

def summoners_info_form(request):

    if request.method == "POST":
        # 소환사명을 검색결과로 받아온다
        summoner_name = request.POST['search_text']
        my_region = 'kr'

        summoners = {
            'summoner_name':summoner_name,
            'my_region':my_region,
        }
        # 검색으로 전적화면으로 넘어가도록
        return redirect(reverse("gg_app:summoners_info", args=[my_region,summoner_name]))

    return redirect(request,'gg_app:index')

def summoners_info(request, country, summoner_name):
    return render(request, "oreumi_gg/summoners.html")






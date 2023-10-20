from django.shortcuts import render, redirect
from django.urls import reverse
from .models import BlogPost
from django.conf import settings
from riotwatcher import LolWatcher, ApiError
from datetime import datetime, timedelta
from dateutil import relativedelta

from .lol_match import match
import requests
import math
# Create your views here.

api_key = getattr(settings, 'API_KEY')
watcher = LolWatcher(api_key)
request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key
}

def index(request):
    return render(request, "oreumi_gg/index.html")
  
def champions(request):
    return render(request, "oreumi_gg/champions.html")

def login(request):
    return render(request, "registration/login.html")

def register(request):
    return render(request, "registration/register.html")

 
def community(request):
    blog_post = BlogPost.objects.all()
    return render(request,"community.html",{"posts":blog_post})
  
  
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
    my_region = country
    myinfo = watcher.summoner.by_name(my_region, summoner_name)
    puuid = myinfo['puuid']
    matches, total_calculate = match(country, puuid, summoner_name)

    context = {
        "matches" : matches, 
        "total_calculate": total_calculate
    }
    return render(request, "oreumi_gg/summoners.html", context)



       
        



from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from .lol_match import match
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

import os, json
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
# Create your views here.

def index(request):
    return render(request, "oreumi_gg/index.html")
  
def champions(request):
    return render(request, "oreumi_gg/champions.html")

def community(request):
    blog_post = BlogPost.objects.all()
    return render(request,"community/community.html",{"posts":blog_post})

# 게시판 목록
def post(request):
    blog_post = BlogPost.objects.all().order_by('-created_at')  # 가장 최근에 생성된 게시글 먼저 나타남
    context = {"posts": blog_post}      
    return render(request, 'community/post_list.html', context)



# 게시글 작정
@login_required
def post_write(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST) 
        if form.is_valid(): # 유효성 검사(필수과정)
            post = form.save()
            post_id = post.id
            return redirect('gg_app:post_detail', post_id=post_id)
        
    # get요청시
    post = BlogPostForm()
    context = {
        'form':post,
        'MEDIA_URL':settings.MEDIA_URL
    }
    return render(request,"community/post_write.html", context)



# 게시글 수정
def post_edit(request, post_id):        
    post = BlogPost.objects.get(pk=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('gg_app:post')  # 수정 후 게시물 목록 페이지로 리디렉션
    else:
        form = BlogPostForm(instance=post)

    return render(request, 'community/post_write_2.html', {'form': form, 'post': post})


# 상세 페이지
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)  # 게시물 가져오기, 없으면 404 에러 발생

    comments = Comment.objects.filter(post=post_id).order_by('-created_date')
    

    return render(request, 'community/post_detail.html', {'post': post, 'comments':comments,'form': CommentForm()})

  
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
    matches, total_calculate, search_player_info_dict = match(country, summoner_name, 0, None)
    context = {
        "matches" : matches, 
        "total_calculate": total_calculate,
        "search_player_info_dict" : search_player_info_dict
    }
    return render(request, "oreumi_gg/summoners.html", context)



def summoners_info_api(request, country, summoner_name, count, queue):
    matches, total_calculate, search_player_info_dict = match(country, summoner_name, count, queue)
    response_data = {
        "matches": matches,
        "total_calculate": total_calculate,
    }
    return JsonResponse(response_data)
  
  
def champion_tier_list(request, position, region, tier):
# Op.gg URL 생성
    opgg_url = "https://www.op.gg/champions?region="+region+"&tier="+tier+"&position="+position
    print(opgg_url)
    # HTTP 요청을 보내서 페이지 내용을 가져옵니다.
    response = requests.get(opgg_url,headers={'User-Agent': 'Mozilla/5.0'})
    response.encoding = 'utf-8'
    print(response)
    if response.status_code == 200:
        # BeautifulSoup를 사용하여 HTML 파싱
        soup = BeautifulSoup(response.text, 'html.parser',from_encoding='utf-8')
        # <tr> 태그를 찾아서 모든 행을 가져옵니다.
        rows = soup.find_all("tr")

        # 헤더 행 제외하고 각 행에서 챔피언의 티어 정보를 추출합니다.
        champion_tiers = []
        for row in rows[1:]:  
            columns = row.find_all("td")
            rank = columns[0].find('span').text.strip()
            champion_img = columns[1].find('img')['src']
            champion_name = columns[1].find('strong').text.strip()
            print(champion_name)
            tier = columns[2].text.strip()
            win_rate = columns[3].text.strip()
            pick_rate = columns[4].text.strip()
            ban_rate = columns[5].text.strip()
            weak_against_champions = []
            weak_against_images = columns[6].find_all('a')
            for weak_against_image in weak_against_images:
                img_tag = weak_against_image.find('img')
                if img_tag:
                    image_url = img_tag['src']
                    weak_against_champions.append(image_url)

            champion_tiers.append({
                'rank' : rank,
                'champion_img': champion_img,
                'champion_name': champion_name,
                'tier' : tier,
                'win_rate': win_rate,
                'pick_rate': pick_rate,
                'ban_rate': ban_rate,
                'weak_against_champions': weak_against_champions,
            })
        print(champion_tiers[0].items())
        return render(request, 'oreumi_gg/champions.html', {'champion_tiers': champion_tiers})
    else:
        return render(request, 'oreumi_gg/champions.html', {'error': '페이지를 불러올 수 없습니다.'})
    
def lotation_list(request):
    champion_file = 'C:/Users/KYS/Desktop/est/Oreumi.gg/champion.json'
    with open(champion_file, 'r',encoding='utf-8') as json_file:
        parsed_data = json.load(json_file)  # JSON 파일을 파싱해서 파이썬 딕셔너리로 읽음
    print(parsed_data["data"]["Aatrox"]["key"])
    url = "https://kr.api.riotgames.com/lol/platform/v3/champion-rotations?api_key="+getattr(settings,"LOL_API" ,"LOL_API")
    response = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    print(response)
    if response.status_code == 200:
        data = response.json()
        free_champion_ids = data["freeChampionIds"]
        champion_names=[]
        champion_eng_names = []
        print(free_champion_ids)
        for data in parsed_data["data"]:
            for champion_id in free_champion_ids:
                champion_id = str(champion_id)
                if champion_id == parsed_data["data"][data]["key"]:
                    champion_names.append(parsed_data["data"][data]["name"])
                    champion_eng_names.append(data)
        combined_champion_names = zip(champion_eng_names, champion_names)
        print(combined_champion_names)
        return render(request, 'oreumi_gg/champions.html', {
            'combined_champion_names': combined_champion_names
        })
    else:
        return render(request, 'oreumi_gg/champions.html',{'error': '페이지를 불러올 수 없습니다.'})
    


def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('gg_app:post_detail', post_id=post_id)

    return redirect('gg_app:post_detail', post_id=post_id)  # 실패 시 동일한 페이지로 리디렉션

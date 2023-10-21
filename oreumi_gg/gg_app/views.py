
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

from .lol_match import match
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
def post_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # 폼이 유효하면 데이터베이스에 저장
            return redirect('gg_app:community')  # 게시글 목록 페이지로 리다이렉트
    else:
        form = BlogPostForm()  # GET 요청인 경우 빈 폼 생성

    return render(request, 'community/post_write.html', {'form': form})


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

    return render(request, 'community/post_edit.html', {'form': form, 'post': post})


# 상세 페이지
def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)  # 게시물 가져오기, 없으면 404 에러 발생
    return render(request, 'community/post_detail.html', {'post': post})

  
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
    matches, total_calculate = match(country, summoner_name, 0)
    context = {
        "matches" : matches, 
        "total_calculate": total_calculate
    }
    return render(request, "oreumi_gg/summoners.html", context)


# 더보기 를 위한 함수
# def summoners_info_api(request, country, summoner_name, start):
#     temp_matches, temp_total_calculate, temp_match_count = match(country, summoner_name, 0)
#     match_count = temp_match_count
#     matches, total_calculate, match_count = match(country, summoner_name, match_count)
#     response_data = {
#         "matches": matches,
#         "total_calculate": total_calculate,
#         "match_count" : match_count
#     }
#     return JsonResponse(response_data)

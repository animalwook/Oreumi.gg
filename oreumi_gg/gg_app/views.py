
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q

from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm
from .lol_match import match
from .ingame_data import find_id, find_league_info, find_spectator_info
import requests
from django.core.paginator import Paginator
from bs4 import BeautifulSoup
import json
from oreumi_gg.settings import get_secret, champion_file
# Create your views here.


def index(request):
    posts=BlogPost.objects.all().order_by('-created_at')
    context = {
        'posts': posts, 
        }
    return render(request, "oreumi_gg/index.html",context)
  
def champions(request):
    return render(request, "oreumi_gg/champions.html")

def modes(request):
    return render(request, "oreumi_gg/modes.html")

# 통계

def statistics_champions(request):
    return render(request, "oreumi_gg/statistics/statistics_champions.html")

def statistics_tier(request):
    return render(request, "oreumi_gg/statistics/statistics_tier.html")

# 랭킹

def leaderboards(request):
    return render(request, "oreumi_gg/leaderboards/leaderboards.html")

def type_champions(request):
    return render(request, "oreumi_gg/leaderboards/type_champions.html")

def type_ladder_flex(request):
    return render(request, "oreumi_gg/leaderboards/type_ladder_flex.html")

def type_ladder(request):
    return render(request, "oreumi_gg/leaderboards/type_ladder.html")

def type_level(request):
    return render(request, "oreumi_gg/leaderboards/type_level.html")




'''
#######################################
커뮤니티 부분
#######################################
'''

def community(request,category="default", order_by="default"):
    posts = BlogPost.objects.all().order_by("-created_at")
    recent_posts=posts    
    tag_on = 'default'
    if order_by !='default':
        if order_by == 'author':
            posts = posts.order_by('author')
            tag_on = 'author'
        elif order_by == 'update':
            posts = posts.order_by('-created_at')
            tag_on = 'update'
        elif order_by == 'view':
            posts = posts.order_by('-view')
            tag_on = 'view'
        elif order_by == 'top':
            posts = posts.order_by('-up')
            tag_on = 'top'


    if category !='default':
        if category == 's':
            category_tag='공지사항'
        elif category == 'tip':
            category_tag='팁과노하우'
        elif category == 'free':
            category_tag='자유게시판'
        elif category == 'art':
            category_tag='팬 아트'
        elif category == 'lfg':
            category_tag='소환사의 협곡'            
        elif category == 'aram':
            category_tag='칼바람 나락'
        elif category == 'tft':
            category_tag='전략적 팀 전투'

        posts = posts.filter(Q(category__icontains=category_tag))
    
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    
    context = {'posts': posts, 'recent_posts':recent_posts,'category':category, 'tag_on':tag_on, 'page_posts': page_posts}

    return render(request,"community/post_list.html", context)

# 게시글 작정
@login_required
def post_write(request):

    if request.method == 'POST':
        form = BlogPostForm(request.POST) 
        if form.is_valid(): # 유효성 검사(필수과정)
            # 현재 로그인한 사용자를 게시물의 저자로 설정
            post = form.save(commit=False)
            post.category = request.POST['category']
            post.author = request.user.nickname  # 사용자의 닉네임으로 설정
   
            #bs4로 파싱해서 경로 가져오기
            img_tag = BeautifulSoup(post.content,'html.parser').find('img')
            if img_tag :
                post.thumbnail = img_tag.get('src')[6:]

            post.save()
            post_id = post.id
            return redirect('gg_app:post_detail', post_id=post_id)
        
    # get요청시
    post = BlogPostForm()
    #에디터의 이미지경로 설정
    context = {
        'form':post,
        'MEDIA_URL':settings.MEDIA_URL,
    }
    return render(request,"community/post_write.html", context)


# 게시글 수정
@login_required
def post_edit(request, post_id):        
    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            #bs4로 파싱해서 경로 가져오기
            img_tag = BeautifulSoup(form.content,'html.parser').find('img')
            if img_tag :
                post.thumbnail = img_tag.get('src')[6:]
            form.save()
            return redirect('gg_app:post_detail', post_id=post_id)  # 수정 후 게시물 목록 페이지로 리디렉션
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'community/post_write.html', {'form': form, 'category':post.category, 'post_id': post.id})

# 게시글 삭제
@login_required
def post_delete(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'GET':
        post.delete()
    return redirect('gg_app:community')  # 수정 후 게시물 목록 페이지로 리디렉션

# 상세 페이지
def post_detail(request, post_id):
    last_record=BlogPost.objects.all().order_by('-id').first().id+1
    if (-1<post_id<last_record) is not True : #혹시나 게시글 번호가 넘어갔을경우
        return  redirect('gg_app:community')
    try:
        post = get_object_or_404(BlogPost, pk=post_id)  # 게시물 가져오기, 없으면 404 에러 발생
        comments = Comment.objects.filter(post=post_id).order_by('created_date')
        post.view +=1
        post.save()
        context = {
            'post': post, 
            'comments':comments,
            'form': CommentForm(), 
            'last_record':last_record,
            }
        return render(request, 'community/post_detail.html', context)
    except:
        post_id -=1
        if post_id == 0 :
                return  redirect('gg_app:community')
        comments = Comment.objects.filter(post=post_id).order_by('created_date')
        post = get_object_or_404(BlogPost, pk=post_id)
        post.view +=1
        post.save()

        context = {
            'post': post, 
            'comments':comments,
            'form': CommentForm(), 
            'last_record':last_record,
            }
        return render(request, 'community/post_detail.html', context)

def add_comment(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            post.comment_count +=1
            post.save()
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.nickname      # 댓글작성자: 닉네임으로 표시하기
            comment.save()
            return redirect('gg_app:post_detail', post_id=post_id)

    return redirect('gg_app:post_detail', post_id=post_id)  # 실패 시 동일한 페이지로 리디렉션

# 검색
def post_search(request):
    search_data = request.GET.get("search_post")
    search_list = BlogPost.objects.filter(
        Q(title__icontains=search_data) | Q(content__icontains=search_data)
    )
    context = {"posts": search_list,"category":'default',"tag_on":'default'}      
    return render(request,"community/post_list.html",context)


# 추천, 비추천 기능
@login_required
def post_like(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.up_list.all():
        post.up_list.remove(request.user)
        post.up -= 1
        post.save()
    else:
        post.up_list.add(request.user)
        post.up += 1
        post.save()
    return redirect('gg_app:post_detail', post_id=post_id)


@login_required
def post_dislike(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.down_list.all():
        post.down_list.remove(request.user)
        post.down -= 1
        post.save()
    else:
        post.down_list.add(request.user)
        post.down += 1
        post.save()
    return redirect('gg_app:post_detail', post_id=post_id)



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
    return render(request, "oreumi_gg/summoners/summoners.html", context)



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
    

def statistics_champions_list(request, position, region, tier, period, mode):
    #OP.gg URL 생성
    opgg_url = "https://www.op.gg/champions?region="+region+"&tier="+tier+"&position="+position+"&period="+period+"&mode="+mode
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
        champion_statistics = []
        for row in rows[1:]:  
            columns = row.find_all("td")
            rank = columns[0].find('span').text.strip()
            champion_img = columns[1].find('img')['src']
            champion_name = columns[1].find('strong').text.strip()
            print(champion_name)
            num_of_plays = columns[2].text.strip()
            rating = columns[3].find('span').text.strip()
            win_rate = columns[4].text.strip()
            pick_rate = columns[5].text.strip()
            ban_rate = columns[6].text.strip()
            cs = columns[7].text.strip()
            gold = columns[8].text.strip()
        
            champion_statistics.append({
                'rank' : rank,
                'champion_img': champion_img,
                'champion_name': champion_name,
                'num_of_plays': num_of_plays,
                'rating' : rating,
                'win_rate': win_rate,
                'pick_rate': pick_rate,
                'ban_rate': ban_rate,
                'cs': cs,
                'gold': gold,
            })
        print(champion_statistics[0].items())
        return render(request, 'oreumi_gg/statistics_champions.html', {'champion_statistics': champion_statistics})
    else:
        return render(request, 'oreumi_gg/statistics_champions.html', {'error': '페이지를 불러올 수 없습니다.'})

def lotation_list(request):
    champion_json_file = champion_file
    with open(champion_json_file, 'r',encoding='utf-8') as json_file:
        parsed_data = json.load(json_file)  # JSON 파일을 파싱해서 파이썬 딕셔너리로 읽음
    print(parsed_data["data"]["Aatrox"]["key"])
    url = "https://kr.api.riotgames.com/lol/platform/v3/champion-rotations?api_key="+get_secret("LOL_API")
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

def ingame(request):
    return render(request, "oreumi_gg/ingame_test.html")

def ingame_info(request,nickname):
    user_id = find_id(nickname)
    user_spectator_info_arr, banned_champion_names = find_spectator_info(user_id)
    blue_data = list(zip(user_spectator_info_arr[:5], banned_champion_names[:5]))
    red_data = list(zip(user_spectator_info_arr[5:], banned_champion_names[5:]))
    print(banned_champion_names[:5])
    print(banned_champion_names[5:])
    context = {
        'blue_data': blue_data,
        'red_data': red_data,
    }
    return render(request, 'oreumi_gg/ingame.html',context)

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




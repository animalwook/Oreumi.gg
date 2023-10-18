from django.shortcuts import render
from .models import BlogPost
from django.conf import settings
from riotwatcher import LolWatcher, ApiError
from datetime import datetime
# Create your views here.
api_key = settings.api_key
watcher = LolWatcher(api_key)

def index(request):
    blog_post = BlogPost.objects.all()
    return render(request,"index.html",{"posts":blog_post})

def search(request, country, summonername):
    my_region = country
    myinfo = watcher.summoner.by_name(my_region, summonername)
    puuid = myinfo['puuid']
    match(country, puuid, summonername)
    return render(request)

def match(country, puuid, summonername):
    # 이미지 가져오는 주소
    # https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/Yone.png
    match_20 = watcher.match.matchlist_by_puuid(country, puuid)
    result_match = []
    for onematch in match_20:
        num = 1
        match_detail = watcher.match.by_id("asia", onematch)
        time = match_detail["info"]["gameEndTimestamp"] / 1000
        game_type = ''
        win_or_not = ''
        search_player_kill = 0
        search_player_assist = 0
        search_player_death = 0
        result = {}
        game_time = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
        if match_detail['info']['queueId'] == 420:
            game_type = "솔랭"
        elif match_detail['info']['queueId'] == 440:
            game_type = "자유 5:5 랭크"
        elif match_detail['info']['queueId'] == 450:
            game_type = "칼바람"
        elif match_detail['info']['queueId'] == 430:
            game_type = "일반"
        elif match_detail['info']['queueId'] in [830, 840, 850]:
            game_type = "ai 대전"
        elif match_detail['info']['queueId'] == 900:
            game_type = "우르프"
        for player_info in match_detail["info"]["participants"]:
            player_dict = {}
            if player_info["summonerName"] == summonername:
                if player_info["win"] == True:
                    win_or_not = "승리"
                else:
                    win_or_not = "패배"

                search_player_kill = player_info["kills"]
                search_player_assist = player_info["assists"]
                search_player_death = player_info["deaths"]
                
            player_dict = [{"kills" : player_info["kills"], "assists" : player_info["assists"], "deaths" : player_info["deaths"],
                           "summonername" : player_info["summonerName"], "championname" : player_info["championName"], 
                           "teamposition" : player_info["teamPosition"], "teamid" : player_info["teamId"]}]
            result[num] = player_dict
            num += 1
        result.update({"time" : time, "game_type" : game_type, "win_or_not" : win_or_not, "search_player_kill" : search_player_kill, "search_player_death" : search_player_death,
                  "search_player_assist" : search_player_assist, "game_time" : game_time}) 
        result_match.append(result)
    return result_match
        
       
        
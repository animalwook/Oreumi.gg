from django.shortcuts import render
from .models import BlogPost
from django.conf import settings
from riotwatcher import LolWatcher, ApiError
from datetime import datetime, timedelta
from dateutil import relativedelta
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
    blog_post = BlogPost.objects.all()
    return render(request,"index.html",{"posts":blog_post})

def search(request, country, summonername):
    my_region = country
    myinfo = watcher.summoner.by_name(my_region, summonername)
    puuid = myinfo['puuid']
    matches = match(country, puuid, summonername)
    return render(request, "search.html", {"matches" : matches})


def timecalculate(time):
    now = datetime.now()
    time_differ = now - time
    seconds = time_differ.total_seconds()
    
    if seconds < 60:
        return "방금 전"
    elif seconds < 3600:
        count = int(seconds / 60)
        return f"{count}분 전"
    elif seconds < 86400:
        count = int(seconds / 3600)
        return f"{count}시간 전"
    elif seconds < 2592000:
        count = int(seconds / 86400)
        return f"{count}일 전"
    else:
        count = int(seconds / 2592000)
        return f"{count}달 전"


# 티어 가져오는 부분 보류(api문제)
# def findtier(country, id):
#     searchplayerinfo = watcher.league.by_summoner(country, id)
#     return searchplayerinfo

def match(country, puuid, summonername):
    summonerSpells = {21 : "SummonerBarrier", 1 : "SummonerBoost", 14 : "SummonerDot", 3 : "SummonerExhaust", 4 : "SummonerFlash",
                  6 : "SummonerHaste", 7 : "SummonerHeal", 13 : "SummonerMana", 30 : "SummonerPoroRecall",
                  31 : "SummonerPoroThrow", 11 : "SummonerSmite", 39 : "SummonerSnowURFSnowball_Mark", 32: "SummonerSnowball",
                  12 : "SummonerTeleport"}
    rune = {8000 : "7201_Precision", 8100 : "7200_Domination", 8200 : "7202_Sorcery", 8300 : "7203_Whimsy", 8400 : "7204_Resolve"}
    # 이미지 가져오는 주소
    # https://ddragon.leagueoflegends.com/cdn/13.20.1/img/champion/Yone.png
    match_20 = watcher.match.matchlist_by_puuid(country, puuid)
    result_match = []
    for onematch in match_20:
        num = 1
        match_detail = watcher.match.by_id("asia", onematch)
        game_playtime_min = match_detail["info"]["gameDuration"] // 60
        game_playtime_sec = match_detail["info"]["gameDuration"] % 60
        game_playtime = f"{game_playtime_min}분 {game_playtime_sec}초" 
        time = match_detail["info"]["gameEndTimestamp"] // 1000
        game_type = ''
        win_or_not = ''
        search_player_kill = 0
        search_player_assist = 0
        search_player_death = 0
        result = {}
        game_time = datetime.fromtimestamp(time)
        game_time = timecalculate(game_time)
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
            # 티어부분 보류(api문제)
            # searchplayerinfo = findtier(country, player_info["summonerId"])
            # if game_type == "솔랭":
            #     if len(searchplayerinfo) == 2:
            #         if searchplayerinfo[0]["queueType"] == "RANKED_SOLO_5x5":
            #             tier = searchplayerinfo[0]["tier"]
            #             rank = searchplayerinfo[0]["rank"]
            #         else:
            #             tier = searchplayerinfo[1]["tier"]
            #             rank = searchplayerinfo[1]["rank"]
            #     else:
            #         tier = searchplayerinfo[0]["tier"]
            #         rank = searchplayerinfo[0]["rank"]
            # elif game_type == "자유 5:5 랭크":
            #     if len(searchplayerinfo) == 2:
            #         if searchplayerinfo[0]["queueType"] == "RANKED_FLEX_SR":
            #             tier = searchplayerinfo[0]["tier"]
            #             rank = searchplayerinfo[0]["rank"]
            #         else:
            #             tier = searchplayerinfo[1]["tier"]
            #             rank = searchplayerinfo[1]["rank"]
            #     else:
            #         tier = searchplayerinfo[0]["tier"]
            #         rank = searchplayerinfo[0]["rank"]
            if player_info["summonerName"] == summonername:
                if player_info["win"] == True:
                    win_or_not = "승리"
                else:
                    win_or_not = "패배"

                search_player_kill = player_info["kills"]
                search_player_assist = player_info["assists"]
                search_player_death = player_info["deaths"]
                search_player_champ = player_info["championName"]
                search_player_kda =  round(player_info["challenges"]["kda"], 2)
                search_player_killpart =  (round(player_info["challenges"]["killParticipation"], 2)) * 100
                search_player_firstrune = player_info["perks"]["styles"][0]["style"]
                search_player_secondrune = player_info["perks"]["styles"][1]["style"]
                for key, value in rune.items():
                    if key == search_player_firstrune:
                        search_player_main_rune = value
                    if key == search_player_secondrune:
                        search_player_sub_rune = value
                for key, value in summonerSpells.items():
                    if key == player_info["summoner1Id"]:
                        search_player_summonerspell1 = value
                    if key == player_info["summoner2Id"]:
                        search_player_summonerspell2 = value
                search_player_item = []
                for i in range(7):
                    search_player_item.append(player_info[f"item{i}"])
                
            totalminions_kill = player_info["totalMinionsKilled"] + player_info["neutralMinionsKilled"]
            first_rune = player_info["perks"]["styles"][0]["style"]
            second_rune = player_info["perks"]["styles"][1]["style"]
            for key, value in rune.items():
                if key == first_rune:
                    main_rune = value
                if key == second_rune:
                    sub_rune = value
            for key, value in summonerSpells.items():
                if key == player_info["summoner1Id"]:
                    summonerspell1 = value
                if key == player_info["summoner2Id"]:
                    summonerspell2 = value
            player_dict = [{"kills" : player_info["kills"], "assists" : player_info["assists"], 
                            "deaths" : player_info["deaths"], "summonername" : player_info["summonerName"], 
                            "championname" : player_info["championName"], "teamposition" : player_info["teamPosition"], 
                            "teamid" : player_info["teamId"], "item0" : player_info["item0"],
                           "item1" : player_info["item1"], "item2" : player_info["item2"], 
                           "item3" : player_info["item3"], "item4" : player_info["item4"],
                           "item5" : player_info["item5"], "item6" : player_info["item6"],
                           "totalminions_kill" : totalminions_kill, "wardsKilled" : player_info["wardsKilled"],
                           "wardsPlaced" : player_info["wardsPlaced"], "visionWardsBoughtInGame" : player_info["visionWardsBoughtInGame"],
                           "summonerspell1" : summonerspell1, "summonerspell2" : summonerspell2, "kda" : round(player_info["challenges"]["kda"], 2),
                           "killparticipation" : round(player_info["challenges"]["killParticipation"], 2), "totalDamageDealtToChampions": player_info["totalDamageDealtToChampions"],
                           "totalDamageTaken" : player_info["totalDamageTaken"], "champlevel" : player_info["champLevel"], 
                           "main_rune" : main_rune, "sub_rune" : sub_rune}]
            result.update({"participant":player_dict}) 
            
        result.update({"game_playtime" : game_playtime, "game_type" : game_type, "win_or_not" : win_or_not, "search_player_kill" : search_player_kill, 
                       "search_player_death" : search_player_death, 
                       "search_player_assist" : search_player_assist, 
                       "game_time" : game_time,
                       "search_player_champ" : search_player_champ,
                       "search_player_kda" : search_player_kda, 
                       "search_player_killpart" : search_player_killpart,
                       "search_player_main_rune" : search_player_main_rune,
                       "search_player_sub_rune" : search_player_sub_rune,
                       "search_player_summonerspell1" : search_player_summonerspell1, 
                       "search_player_summonerspell2" : search_player_summonerspell2,
                       "search_player_item" : search_player_item}) 
        result_match.append(result)
    return result_match
        
       
        
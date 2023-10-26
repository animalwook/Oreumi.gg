from django.conf import settings
from riotwatcher import LolWatcher, ApiError
from datetime import datetime
import requests
import math
import decimal


summonerSpells = {21 : "SummonerBarrier", 1 : "SummonerBoost", 14 : "SummonerDot", 
                  3 : "SummonerExhaust", 4 : "SummonerFlash",6 : "SummonerHaste", 
                  7 : "SummonerHeal", 13 : "SummonerMana", 30 : "SummonerPoroRecall",
                31 : "SummonerPoroThrow", 11 : "SummonerSmite", 39 : "SummonerSnowURFSnowball_Mark", 
                32: "SummonerSnowball", 12 : "SummonerTeleport", 2202 : "SummonerCherryFlash", 
                2201 : "SummonerCherryHold", 54 : "Summoner_UltBookPlaceholder", 55 : "Summoner_UltBookSmitePlaceholder", 0 : "arena"}

rune = {8000 : "7201_Precision", 8100 : "7200_Domination", 8200 : "7202_Sorcery", 8300 : "7203_Whimsy", 8400 : "7204_Resolve"}
# 룬 정보를 담고 있는 url
url = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perks.json"
response = requests.get(url)
rune_data = response.json()

def roundup(num):
    """
    소수점 첫째자리까지 나오게하는 함수 (0.5까지 올림)
    """
    num = round(num, 2)
    if len(str(num - 0.05).split('.')[1]) == 1:
        return math.ceil(num * 10) / 10
    elif int(num) + 1 == int(round(num, 1)):
        return math.floor(num * 10) / 10
    else:
        return float('{:.1f}'.format(num))
    
def roundup2(num):
    """
    소수점 둘째자리까지 나오게 하는 함수 (0.05까지 올림)
    """
    num = round(num, 3)
    if len(str(num - 0.005).split('.')[1]) == 2:
        return math.ceil(num * 100) / 100
    else:
        return float('{:.2f}'.format(num))
    
def capitalize_first_letter(input_string):
    """ 
    첫 글자만 대문자로 하고 나머지 글자는 소문자로 바꾸는 함수
    """
    # 문자열이 비어 있는지 확인
    if not input_string:
        return input_string

    # 문자열의 첫 글자를 대문자로, 나머지를 소문자로 변환
    if input_string == "FiddleSticks":
        result_string = input_string[0].upper() + input_string[1:].lower()
    else:
        result_string = input_string
    
    return result_string

def calculateminperminion(sec, kill, min):
    """ 
    분당 cs(미니언) 계산
    """
    result = 0
    if sec >= 45:
        result = roundup(kill / (min + 1))
    elif sec >= 15:
        result = roundup(kill / (min + 0.5))
    else:
        result = roundup(kill / min)
    return result

def timecalculate(time):
    """
    시간 계산 함수 X 일 전, X 시간 전 등으로 변경하는 함수
    """
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

api_key = getattr(settings, 'API_KEY')
watcher = LolWatcher(api_key)

def summoner_info(country, myinfo):
    
    # 크로링에서 db로 전향 필요
    my_league_info = watcher.league.by_summoner(country, myinfo['id'])
    """
    [
    {
        "leagueId": "548cecb1-3868-4916-96c2-3625202e8e05",
        "queueType": "RANKED_SOLO_5x5",
        "tier": "SILVER",
        "rank": "II",
        "summonerId": "EE2eARX3pTxgPB8AV1jbfjR8N0IrTRRrULzJxKDwX0rPeNo",
        "summonerName": "거니라구",
        "leaguePoints": 51,
        "wins": 4,
        "losses": 5,
        "veteran": false,
        "inactive": false,
        "freshBlood": false,
        "hotStreak": false
    }
    ]
    """
    # 크롤링에서 db로 전향 필요
    search_player_tear_by_season = "크롤링필요"
    my_summoner_ranking = "크롤링필요",
    
    # 랭크 여부 확인
    if len(my_league_info) == 0 : # 랭크를 하지 않음
            search_player_solo_tear = None
            search_player_solo_rank = None
            search_player_solo_points = None
            search_player_solo_wins = None
            search_player_solo_losses = None
            search_player_flex_tear = None
            search_player_flex_rank = None
            search_player_flex_points = None
            search_player_flex_wins = None
            search_player_flex_losses = None
    elif len(my_league_info) == 1 : # 솔로인지 자유랭인지 확인

        if my_league_info[0].get('queueType') == "RANKED_SOLO_5x5":
            search_player_solo_tear = my_league_info[0].get('tier')
            search_player_solo_rank = my_league_info[0].get('rank')
            search_player_solo_points = my_league_info[0].get('leaguePoints')
            search_player_solo_wins = my_league_info[0].get('wins')
            search_player_solo_losses = my_league_info[0].get('losses')
            search_player_flex_tear = None
            search_player_flex_rank = None
            search_player_flex_points = None
            search_player_flex_wins = None
            search_player_flex_losses = None
        else :
            search_player_solo_tear = None
            search_player_solo_rank = None
            search_player_solo_points = None
            search_player_solo_wins = None
            search_player_solo_losses = None
            search_player_flex_tear = my_league_info[0].get('tier')
            search_player_flex_rank = my_league_info[0].get('rank')
            search_player_flex_points = my_league_info[0].get('leaguePoints')
            search_player_flex_wins = my_league_info[0].get('wins')
            search_player_flex_losses = my_league_info[0].get('losses')

    elif len(my_league_info) == 2 : # 솔랭/자유랭크 있음
        search_player_solo_tear = my_league_info[0].get('tier')
        search_player_solo_rank = my_league_info[0].get('rank')
        search_player_solo_points = my_league_info[0].get('leaguePoints')
        search_player_solo_wins = my_league_info[0].get('wins')
        search_player_solo_losses = my_league_info[0].get('losses')
        search_player_flex_tear = my_league_info[1].get('tier')
        search_player_flex_rank = my_league_info[1].get('rank')
        search_player_flex_points = my_league_info[1].get('leaguePoints')
        search_player_flex_wins = my_league_info[1].get('wins')
        search_player_flex_losses = my_league_info[1].get('losses')

    search_player_solo = {
        'search_player_solo_tear' : search_player_solo_tear,
        'search_player_solo_rank' : search_player_solo_rank,
        'search_player_solo_points' : search_player_solo_points,
        'search_player_solo_wins': search_player_solo_wins,
        'search_player_solo_losses': search_player_solo_losses,
    }
    search_player_flex = {
        'search_player_flex_tear' : search_player_flex_tear,
        'search_player_flex_rank' : search_player_flex_rank,
        'search_player_flex_points' : search_player_flex_points,
        'search_player_flex_wins': search_player_flex_wins,
        'search_player_flex_losses': search_player_flex_losses,
    }

    search_player_info_dict = {
        'search_player_tear_by_season' : search_player_tear_by_season ,
        'search_player_ranking' : my_summoner_ranking,
        'search_player_name' :  myinfo['name'],
        'search_player_icon' :  myinfo['profileIconId'],
        'search_player_level' :  myinfo['summonerLevel'],
    }
    search_player_info_dict.update(search_player_solo)
    search_player_info_dict.update(search_player_flex)

    return search_player_info_dict


def match(country, summonername, start, queue):
    my_region = country
    lower_summoner_name = summonername.lower().replace(' ', '')
    myinfo = watcher.summoner.by_name(my_region, lower_summoner_name)

    # 최상단에 들어가는 소환사 정보
    search_player_info_dict = summoner_info(country,myinfo)

    puuid = myinfo['puuid']
    summonerid = myinfo['id']
    # 사용자 puuid와 country를 이용하여 최근 20경기 정보를 가져옴
    if queue == 9999:
        match_20 = watcher.match.matchlist_by_puuid(country, puuid, start)
    else:
        match_20 = watcher.match.matchlist_by_puuid(country, puuid, start, 20, queue)
    result_match = []
    win_count = 0
    total_match_count = 0
    lose_count = 0
    total_kill = 0
    total_death = 0
    total_assist = 0
    total_kill_part = 0

    for onematch in match_20:
        match_detail = watcher.match.by_id("asia", onematch)
        num = 1
        game_playtime_min = match_detail["info"]["gameDuration"] // 60
        game_playtime_sec = match_detail["info"]["gameDuration"] % 60
        game_playtime = f"{game_playtime_min}분 {game_playtime_sec}초" 
        time = match_detail["info"]["gameEndTimestamp"] // 1000
        game_type = ''
        win_or_not = ''
        win_or_not_eng = ''
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
        elif match_detail['info']['queueId'] == 1700:
            game_type = "아레나"
            
        # 한 경기당 플레이어 10명의 정보를 for문을 사용해 받아옴
        for player_info in match_detail["info"]["participants"]:
            player_dict = {}
            # 티어부분 보류(api문제)
            
            # 검색한 사용자의 정보를 가져옴
            if player_info["summonerId"] == summonerid:
                if player_info["win"] == True:
                    if game_playtime_min <= 3:
                        win_or_not = "다시하기"
                        total_match_count += 1
                        win_or_not_eng = "repeat"
                    else:
                        win_or_not = "승리"
                        win_count += 1
                        total_match_count += 1
                        win_or_not_eng = "victory"
                else:
                    if game_playtime_min <= 3:
                        win_or_not = "다시하기"
                        total_match_count += 1
                        win_or_not_eng = "repeat"
                    else:
                        win_or_not = "패배"
                        lose_count += 1
                        total_match_count += 1
                        win_or_not_eng = "defeat"
                # search_player로 시작하는 것은 검색한 사용자의 정보를 저장하는 변수들
                search_player_kill = player_info["kills"]
                search_player_assist = player_info["assists"]
                search_player_death = player_info["deaths"]
                search_player_champ = capitalize_first_letter(player_info["championName"])
                    
                try:
                    search_value = player_info["challenges"]["killParticipation"]
                    search_player_killpart = round(roundup2(search_value) * 100)
                    search_player_kda =  roundup2(player_info["challenges"]["kda"])
                except KeyError:
                    search_player_killpart = 0
                    if search_player_death == 0:
                        search_player_kda = "Perfect"
                    else:
                        search_player_kda = roundup2((search_player_kill + search_player_assist) / search_player_death)
                    
                search_player_champlevel = player_info["champLevel"]
                search_player_firstrune = player_info["perks"]["styles"][0]["selections"][0]["perk"]
                search_player_secondrune = player_info["perks"]["styles"][1]["style"]
                search_player_totalminions_kill = player_info["totalMinionsKilled"] + player_info["neutralMinionsKilled"]
                search_player_visionWardsBoughtInGame = player_info["visionWardsBoughtInGame"]
                search_player_minperminions = calculateminperminion(game_playtime_sec, search_player_totalminions_kill, game_playtime_min)
                search_player_main_rune = ''
                search_player_sub_rune = ''
                for item in rune_data:
                    if item.get("id") == search_player_firstrune:
                        search_player_main_rune = item.get("iconPath").split("v1/")[1]
                        break
                
                for key, value in rune.items():
                    if key == search_player_secondrune:
                        search_player_sub_rune = value
                for key, value in summonerSpells.items():
                    if key == player_info["summoner1Id"]:
                        search_player_summonerspell1 = value
                    if key == player_info["summoner2Id"]:
                        search_player_summonerspell2 = value
                search_player_item = []
                
                # 아이템은 총 7개 존재
                for i in range(7):
                    search_player_item.append(player_info[f"item{i}"])
                
                total_kill += search_player_kill
                total_death += search_player_death
                total_assist += search_player_assist
                total_kill_part += search_player_killpart
                
            # 총 미니언 수는 중립 미니언과 일반 미니언 수를 합친 결과
            totalminions_kill = player_info["totalMinionsKilled"] + player_info["neutralMinionsKilled"]
            minperminions = calculateminperminion(game_playtime_sec, totalminions_kill, game_playtime_min)
            # 메인 룬의 경우 정복자, 치속 등으로 나오지만 서브룬은 룬의 카테고리로나옴
            first_rune = player_info["perks"]["styles"][0]["selections"][0]["perk"]
            second_rune = player_info["perks"]["styles"][1]["style"]
            main_rune = 'none'
            placement = 0
            if player_info.get("placement"):
                placement = player_info["placement"]
            sub_rune = 'none'
            for item in rune_data:
                if item.get("id") == first_rune:
                    main_rune = item.get("iconPath").split("v1/")[1]
                    break
            
            for key, value in rune.items():
                if key == second_rune:
                    sub_rune = value
                    
            for key, value in summonerSpells.items():
                if key == player_info["summoner1Id"]:
                    summonerspell1 = value
                if key == player_info["summoner2Id"]:
                    summonerspell2 = value
            
            try:
                value = player_info["challenges"]["killParticipation"]
                player_kill_part = round(roundup2(value) * 100)
                kda = roundup2(player_info["challenges"]["kda"])
            except KeyError:
                player_kill_part = 0
                if player_info["deaths"] == 0:
                    kda = "Perfect"
                else:
                    kda = roundup2((player_info["kills"] + player_info["assists"]) / player_info["deaths"])
            # 각 플레이어마다 해당 정보 저장
            player_dict = [{"kills" : player_info["kills"], "assists" : player_info["assists"], 
                            "deaths" : player_info["deaths"], "summonername" : player_info["summonerName"], 
                            "championname" : capitalize_first_letter(player_info["championName"]), "teamposition" : player_info["teamPosition"], 
                            "teamid" : player_info["teamId"], "item0" : player_info["item0"],
                        "item1" : player_info["item1"], "item2" : player_info["item2"], 
                        "item3" : player_info["item3"], "item4" : player_info["item4"],
                        "item5" : player_info["item5"], "item6" : player_info["item6"],
                        "totalminions_kill" : totalminions_kill, "wardsKilled" : player_info["wardsKilled"],
                        "wardsPlaced" : player_info["wardsPlaced"], "visionWardsBoughtInGame" : player_info["visionWardsBoughtInGame"],
                        "summonerspell1" : summonerspell1, "summonerspell2" : summonerspell2, "kda" : kda,
                        "killparticipation" : player_kill_part, "totalDamageDealtToChampions": player_info["totalDamageDealtToChampions"],
                        "totalDamageTaken" : player_info["totalDamageTaken"], "champlevel" : player_info["champLevel"], 
                        "main_rune" : main_rune, "sub_rune" : sub_rune, "minperminions" : minperminions, "placement": placement,
                        "goldearned" : player_info["goldEarned"], "win":player_info["win"]}]
            result[num] = player_dict
            num += 1
        result.update({"game_playtime" : game_playtime, "game_type" : game_type, "win_or_not" : win_or_not, "win_or_not_eng" : win_or_not_eng,
                    "search_player_kill" : search_player_kill, 
                    "search_player_death" : search_player_death, 
                    "search_player_assist" : search_player_assist, 
                    "game_time" : game_time,
                    "search_player_champ" : search_player_champ,
                    "search_player_kda" : search_player_kda, 
                    "search_player_killpart" : int(search_player_killpart),
                    "search_player_main_rune" : search_player_main_rune,
                    "search_player_sub_rune" : search_player_sub_rune,
                    "search_player_summonerspell1" : search_player_summonerspell1, 
                    "search_player_summonerspell2" : search_player_summonerspell2,
                    "search_player_item" : search_player_item,
                    "search_player_champlevel" : search_player_champlevel,
                    "search_player_totalminions_kill" : search_player_totalminions_kill,
                    "search_player_visionWardsBoughtInGame" : search_player_visionWardsBoughtInGame,
                    "search_player_minperminions" : search_player_minperminions
        }) 
        result_match.append(result)
            
    win_rate = int(roundup2(win_count / (win_count + lose_count)) * 100)
    total_kill = roundup(total_kill / 20)
    total_death = roundup(total_death / 20)
    total_assist = roundup(total_assist / 20)
    total_kda = roundup2((total_kill + total_assist) / total_death)
    total_calculate = {"win_count" : win_count, "lose_count" : lose_count, 
                    "win_rate" : win_rate, "total_kill" : total_kill, 
                    "total_death" : total_death, "total_assist" : total_assist,
                    "total_match_count" : total_match_count,
                    "total_kda" : total_kda, "total_kill_part" : total_kill_part // 20}    
    return result_match, total_calculate, search_player_info_dict

        
        
# 티어 가져오는 부분 보류(api문제)
# def findtier(country, id):
#     searchplayerinfo = watcher.league.by_summoner(country, id)
#     return searchplayerinfo        




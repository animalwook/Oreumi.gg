from django.conf import settings
from riotwatcher import LolWatcher, ApiError
from datetime import datetime
import requests
import math
from django.http import HttpResponseRedirect
from django.urls import reverse


api_key = getattr(settings, 'API_KEY')
watcher = LolWatcher(api_key)

summonerSpells = {21 : "SummonerBarrier", 1 : "SummonerBoost", 14 : "SummonerDot", 
                  3 : "SummonerExhaust", 4 : "SummonerFlash",6 : "SummonerHaste", 
                  7 : "SummonerHeal", 13 : "SummonerMana", 30 : "SummonerPoroRecall",
                31 : "SummonerPoroThrow", 11 : "SummonerSmite", 39 : "SummonerSnowURFSnowball_Mark", 
                32: "SummonerSnowball", 12 : "SummonerTeleport", 2202 : "SummonerCherryFlash", 
                2201 : "SummonerCherryHold", 54 : "Summoner_UltBookPlaceholder", 55 : "Summoner_UltBookSmitePlaceholder", 0 : "arena"}

rune = {8000 : "7201_Precision", 8100 : "7200_Domination", 8200 : "7202_Sorcery", 8300 : "7203_Whimsy", 8400 : "7204_Resolve"}

url_rune = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perks.json"
response_rune = requests.get(url_rune)
rune_data = response_rune.json()

url_champion = "https://ddragon.leagueoflegends.com/cdn/13.21.1/data/ko_KR/champion.json"
response_champion = requests.get(url_champion)
champion_data = response_champion.json()

def find_id(nickname):
    lower_summoner_name = nickname.lower().replace(' ', '')
    user_info = watcher.summoner.by_name("kr", lower_summoner_name)
    if user_info is None:
        return None
    user_id = user_info['id']
    return user_id

def find_league_info(user_id):
    league_info = watcher.league.by_summoner("kr", user_id)
    
    for league in league_info:
        if league['queueType'] == "RANKED_SOLO_5x5":
            per = league['wins'] / (league['wins'] + league['losses']) * 100
            user_league_info = {
                'tier': league['tier'],
                'rank': league['rank'],
                'rank_odds': f"{per:.0f}%"
            }
            return user_league_info
        
class IngameDataNotFoundError(Exception):
    pass

def find_spectator_info(user_id):
    try:
        user_spectator_info_arr = []
        spectator_info = watcher.spectator.by_summoner("kr", user_id)
        for info in spectator_info["participants"]:
            league_info = find_league_info(info["summonerId"])
            for data in champion_data["data"]:
                champion_id = info['championId']
                champion_id = str(champion_id)
                if champion_id == champion_data["data"][data]["key"]:
                    champion_eng_names = data
                    break
                    
                    
            for item in rune_data:
                if item.get("id") == info["perks"]['perkIds'][0]:
                    main_rune = item.get("iconPath").split("v1/")[1]
                    break         
                
            for key, value in rune.items():
                if key == info["perks"]['perkSubStyle']:
                    sub_rune = value
                    print(sub_rune)      
                    
            for key, value in summonerSpells.items():
                if key == info["spell1Id"]:
                    summonerspell1 = value
                    print(summonerspell1)
                if key == info["spell2Id"]:
                    summonerspell2 = value
                    print(summonerspell2)  
                    
            user_spectator_info_arr.append({
            'champion_eng_name': champion_eng_names,
            'spell1Id': summonerspell1,
            'spell2Id': summonerspell2,
            'perkStyle': main_rune,
            'perkSubStyle': sub_rune,
            'nickname': info['summonerName'],
            'tier': league_info['tier'],
            'rank': league_info['rank'],
            'rank_odds': league_info['rank_odds'],
            }) 
        banned_champions = spectator_info['bannedChampions']
        banned_champion_names = []
        for banned_champion in banned_champions:
            champion_id = banned_champion["championId"]
            champion_id = str(champion_id)
            if champion_id == "-1":
                banned_champion_names.append("")  # 빈 문자열 추가
            else:
                for data in champion_data["data"]:
                    if champion_data["data"][data]["key"] == champion_id:
                        champion_name = data
                        banned_champion_names.append(champion_name)
    except Exception as e:
        if "404 Client Error: Not Found" in str(e):
            raise IngameDataNotFoundError

    return user_spectator_info_arr, banned_champion_names
        


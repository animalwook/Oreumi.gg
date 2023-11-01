from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from user_app.models import User
from django.conf import settings
# Create your models here.



class BlogPost(models.Model):
    title = models.CharField(max_length=200) 
    content = CKEditor5Field('Text', config_name='extends') # 에디터로 바뀔예정
    author = models.CharField(max_length=200,default="admin") # 나중에 외래키로
    view = models.IntegerField(default=0)
    category = models.CharField(max_length=64, default="자유게시판") 
    # images = models.ImageField(null=True,upload)
    # video =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

    thumbnail = models.ImageField(upload_to='',null=True,blank=True)  # 이미지 필드 추가

    up_list = models.ManyToManyField(User, related_name='likes',blank=True)
    down_list = models.ManyToManyField(User, related_name='dislikes',blank=True)

    # 합산 값 
    @property                   # 데코레이터 사용하기 
    def net_count(self):
        return self.up - self.down

    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, default="User")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) 


class ChatRoom(models.Model):
    room_number = models.AutoField(primary_key=True)
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    created_at = models.DateTimeField(auto_now_add=True)
    latest_message_time = models.DateTimeField(null=True, blank=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='chat_rooms', null=True, blank=True)


    def __str__(self):
        return f'ChatRoom: {self.starter.username} and {self.receiver.username}'

class Message(models.Model):
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    #확인을 위해서 넣음
    receiver = models.IntegerField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message: {self.author.username} at {self.timestamp}'

    class Meta:
        ordering = ['timestamp']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 새 메시지가 저장될 때마다 chatroom의 latest_message_time을 업데이트
        self.chatroom.latest_message_time = self.timestamp
        self.chatroom.save()




#소환사정보
class SoloRankList(models.Model):
    rank = models.PositiveIntegerField() 
    summoners = models.CharField(max_length=20, null=True, blank=True)
    tier = models.CharField(max_length=10, null=True, blank=True)
    LP = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    win = models.PositiveIntegerField() 
    lose = models.PositiveIntegerField() 
    most1 = models.CharField(max_length=80, null=True, blank=True)
    most2 = models.CharField(max_length=80, null=True, blank=True)
    most3 = models.CharField(max_length=80, null=True, blank=True)
    
class SummonerModel(models.Model):
    search_player_tear_by_season = models.CharField(max_length=200)
    search_player_ranking = models.PositiveIntegerField()
    search_player_name = models.CharField(max_length=20)
    search_player_icon = models.CharField(max_length=200)
    search_player_level = models.PositiveIntegerField()
    search_player_updated_at = models.DateTimeField(auto_now=True)
    search_player_is_read = models.BooleanField(default=False) #없어도 되는데 임시로 넣음

    search_player_solo_tear = models.CharField(max_length=80, null=True, blank=True)
    search_player_solo_rank = models.CharField(max_length=10, null=True, blank=True)
    search_player_solo_points = models.PositiveIntegerField(null=True, blank=True)
    search_player_solo_wins = models.PositiveIntegerField(null=True, blank=True)
    search_player_solo_losses = models.PositiveIntegerField(null=True, blank=True)
    search_player_flex_tear = models.CharField(max_length=80, null=True, blank=True)
    search_player_flex_rank = models.CharField(max_length=10, null=True, blank=True)
    search_player_flex_points = models.PositiveIntegerField(null=True, blank=True)
    search_player_flex_wins = models.PositiveIntegerField(null=True, blank=True)
    search_player_flex_losses = models.PositiveIntegerField(null=True, blank=True)
    most1 = models.CharField(max_length=80, default="")
    most2 = models.CharField(max_length=80, default="")
    most3 = models.CharField(max_length=80, default="")

class MatchIDModel(models.Model):
    matchId = models.CharField(max_length=200)
    matchSummonerList = models.CharField(max_length=255, default="")
    game_type =models.CharField(max_length=30)

# 해당 게임의 검색한 소환사에 대한 정보
class MatchInfoForSearchPlayer(models.Model):
    matchId = models.ForeignKey(MatchIDModel, on_delete=models.CASCADE) # matchid에 연결 OneToMany
    summonername = models.CharField(max_length=20)
    
    game_playtime = models.CharField(max_length=20,null=True,blank=True)
    game_type = models.CharField(max_length=20,null=True,blank=True)
    win_or_not = models.CharField(max_length=20,null=True,blank=True)
    win_or_not_eng = models.CharField(max_length=20,null=True,blank=True)
    search_player_kill = models.PositiveIntegerField(null=True,blank=True)
    search_player_death = models.PositiveIntegerField(null=True,blank=True)
    search_player_assist = models.PositiveIntegerField(null=True,blank=True)
    game_time = models.CharField(max_length=20,null=True,blank=True)
    search_player_champ = models.CharField(max_length=20,null=True,blank=True)
    search_player_kda = models.FloatField(null=True,blank=True)
    search_player_killpart = models.PositiveIntegerField(null=True,blank=True)
    search_player_main_rune = models.CharField(max_length=100,null=True,blank=True)
    search_player_sub_rune = models.CharField(max_length=20,null=True,blank=True)
    search_player_summonerspell1 = models.CharField(max_length=20,null=True,blank=True)
    search_player_summonerspell2 = models.CharField(max_length=20,null=True,blank=True)
    search_player_item = models.TextField(null=True,blank=True)
    search_player_champlevel = models.PositiveIntegerField(null=True,blank=True)
    search_player_totalminions_kill = models.PositiveIntegerField(null=True,blank=True)
    search_player_visionWardsBoughtInGame =  models.PositiveIntegerField(null=True,blank=True)
    search_player_minperminions = models.FloatField(null=True,blank=True)



# 해당 게임의 모든 플레이어에 대한 자세한 정보
class MatchInfoDetail(models.Model):
    playernumber = models.PositiveIntegerField() #1~10
    matchId = models.ForeignKey(MatchIDModel, on_delete=models.CASCADE) # matchid에 연결 OneToMany
    kills = models.PositiveIntegerField(null=True,blank=True)
    assists = models.PositiveIntegerField(null=True,blank=True)
    deaths = models.PositiveIntegerField(null=True,blank=True)
    summonername = models.CharField(max_length=20,null=True,blank=True)
    championname = models.CharField(max_length=20,null=True,blank=True)
    teamposition = models.CharField(max_length=10,null=True,blank=True)
    teamid = models.PositiveIntegerField(null=True,blank=True)
    item0 = models.PositiveIntegerField(null=True,blank=True)
    item1 = models.PositiveIntegerField(null=True,blank=True)
    item2 = models.PositiveIntegerField(null=True,blank=True)
    item3 = models.PositiveIntegerField(null=True,blank=True)
    item4 = models.PositiveIntegerField(null=True,blank=True)
    item5 = models.PositiveIntegerField(null=True,blank=True)
    item6 = models.PositiveIntegerField(null=True,blank=True)
    totalminions_kill = models.PositiveIntegerField(null=True,blank=True)
    wardsKilled = models.PositiveIntegerField(null=True,blank=True)
    wardsPlaced = models.PositiveIntegerField(null=True,blank=True)
    visionWardsBoughtInGame = models.PositiveIntegerField(null=True,blank=True)
    summonerspell1 = models.CharField(max_length=20,null=True,blank=True)
    summonerspell2 = models.CharField(max_length=20,null=True,blank=True)
    kda = models.FloatField(null=True,blank=True)
    killparticipation = models.PositiveIntegerField(null=True,blank=True)
    totalDamageDealtToChampions = models.PositiveIntegerField(null=True,blank=True)
    totalDamageTaken = models.PositiveIntegerField(null=True,blank=True)
    champlevel = models.PositiveIntegerField(null=True,blank=True)
    main_rune = models.CharField(max_length=200,null=True,blank=True)
    sub_rune = models.CharField(max_length=200,null=True,blank=True)
    minperminions = models.FloatField(null=True,blank=True)
    placement = models.FloatField(null=True,blank=True)
    goldearned = models.PositiveIntegerField(null=True,blank=True)
    win = models.BooleanField(null=True,blank=True)
    dragon_kills = models.PositiveIntegerField(null=True,blank=True)
    turret_kills = models.PositiveIntegerField(null=True,blank=True)
    baron_kills = models.PositiveIntegerField(null=True,blank=True)

    
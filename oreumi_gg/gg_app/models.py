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
    
class summoner(models.Model):
    summoners = models.CharField(max_length=20)
    level = models.PositiveIntegerField()
    ladderLank = models.PositiveIntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)

    solo_tear = models.CharField(max_length=80, null=True, blank=True)
    solo_rank = models.PositiveIntegerField(null=True, blank=True)
    solo_points = models.PositiveIntegerField(null=True, blank=True)
    solo_wins = models.PositiveIntegerField(null=True, blank=True)
    solo_losses = models.PositiveIntegerField(null=True, blank=True)
    flex_tear = models.CharField(max_length=80, null=True, blank=True)
    flex_rank = models.PositiveIntegerField(null=True, blank=True)
    flex_points = models.PositiveIntegerField(null=True, blank=True)
    flex_wins = models.PositiveIntegerField(null=True, blank=True)
    flex_losses = models.PositiveIntegerField(null=True, blank=True)
    most1 = models.CharField(max_length=80, null=True, blank=True)
    most2 = models.CharField(max_length=80, null=True, blank=True)
    most3 = models.CharField(max_length=80, null=True, blank=True)
class match(models.Model):
    matchId = models.CharField(max_length=200)
    matchSummonerList = models.CharField(max_length=255)
class matchInfoSummoner(models.Model):
    match = models.ForeignKey(match, on_delete=models.CASCADE)
    kill = models.PositiveIntegerField()
    assists = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    summonername = models.CharField(max_length=20)
    championname = models.CharField(max_length=20)
    teamposition = models.CharField(max_length=10)
    teamid = models.PositiveIntegerField()
    item0 = models.PositiveIntegerField()
    item1 = models.PositiveIntegerField()
    item2 = models.PositiveIntegerField()
    item3 = models.PositiveIntegerField()
    item4 = models.PositiveIntegerField()
    item5 = models.PositiveIntegerField()
    item6 = models.PositiveIntegerField()
    totalminions_kill = models.PositiveIntegerField()
    wardsKilled = models.PositiveIntegerField()
    wardsPlaced = models.PositiveIntegerField()
    visionWardsBoughtInGame = models.PositiveIntegerField()
    summonerspell1 = models.CharField(max_length=20)
    summonerspell2 = models.CharField(max_length=20)
    kda = models.DecimalField(max_digits=5, decimal_places=2)
    killparticipation = models.PositiveIntegerField()
    totalDamageDealtToChampions = models.PositiveIntegerField()
    totalDamageTaken = models.PositiveIntegerField()
    champlevel = models.PositiveIntegerField()
    main_rune = models.CharField(max_length=200)
    sub_rune = models.CharField(max_length=200)
    minperminions = models.DecimalField(max_digits=5, decimal_places=2)
    placement = models.DecimalField(max_digits=5, decimal_places=2)
    goldearned = models.PositiveIntegerField()
    win = models.BooleanField()
    dragon_kills = models.PositiveIntegerField()
    turret_kills = models.PositiveIntegerField()
    baron_kills = models.PositiveIntegerField()
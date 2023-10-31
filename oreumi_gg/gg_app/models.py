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

    def __str__(self):
        return f'Message: {self.author.username} at {self.timestamp}'

    class Meta:
        ordering = ['timestamp']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # 새 메시지가 저장될 때마다 chatroom의 latest_message_time을 업데이트
        self.chatroom.latest_message_time = self.timestamp
        self.chatroom.save()
from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User  # User 모델을 임포트
from django.conf import settings
# Create your models here.



class BlogPost(models.Model):
    title = models.CharField(max_length=200,) 
    content = CKEditor5Field('Text', config_name='extends') # 에디터로 바뀔예정

    author = models.CharField(max_length=200,default="admin") # 나중에 외래키로
    view = models.IntegerField(default=0)
    category = models.CharField(max_length=64, default="기본") 
    # images = models.ImageField(null=True,upload)
    # video =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    thumnail = models.ImageField(upload_to='images/',null=True,blank=True)  # 이미지 필드 추가
    # 합산 값 
    @property                   # 데코레이터 사용하기 
    def net_count(self):
        return self.up - self.down

    

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, default="User")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) 


# 추천 중복방지
class UserLiked(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    liked = models.BooleanField(default=False)  # True for 추천, False for 비추천

    class Meta:
        unique_together = ('user', 'post')  # 중복 방지
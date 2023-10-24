from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200,) 
    content = models.TextField() # 에디터로 바뀔예정

    author = models.CharField(max_length=200,default="admin") # 나중에 외래키로
    view = models.IntegerField(default=0)
    category = models.CharField(max_length=64, default="기본") 
    # images = models.ImageField(null=True,upload)
    # video =
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)
    # image = models.ImageField(upload_to='images/')  # 이미지 필드 추가
    comments = models.ManyToManyField('Comment', related_name='blog_posts')

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.CharField(max_length=255, default="User")
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)



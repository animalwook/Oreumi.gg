
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(verbose_name="닉네임", max_length=15, unique=True, null=True)
    profil = models.ImageField(verbose_name="프로필", upload_to="user_profil", default="user_profil/oreumi-long.png", null=True)
    exp = models.IntegerField(verbose_name="경험치", default=0, null=True)
    is_staff = models.BooleanField(default=True)

    def __str__(self):
        return self.email
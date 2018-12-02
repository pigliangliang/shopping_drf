from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
# Create your models here.


class UserProfile(AbstractUser):

    """
    用户信息
    """
    gender = (
        ('1','男'),
        ('2','女'),
    )
    name = models.CharField('姓名',max_length=64)
    sex  = models.CharField(choices=gender,max_length=32)
    email =  models.EmailField(max_length=64)
    mobil = models.CharField(max_length=11)

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.username



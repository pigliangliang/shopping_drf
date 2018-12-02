from django.db import models
from users.models import UserProfile
from goods.models import Goods
from datetime import datetime
from django.contrib.auth import get_user_model
user =get_user_model()
# Create your models here.


class UserAddress(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    province = models.CharField(default='',max_length=32,help_text="省")
    city = models.CharField(default='', max_length=32, help_text="市")
    street= models.CharField(default='',max_length=64,help_text='街道')
    signer = models.CharField(max_length=32)
    mobile = models.CharField(max_length=11)

    class Meta:
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}{}{}".format(self.province,self.city,self.street)


class UserFav(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.name


class UserMessage(models.Model):
    user = models.ForeignKey(user,on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE)
    message = models.TextField("留言内容", default="", help_text="留言内容")
    add_time = models.DateTimeField("添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message
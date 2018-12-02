from django.db import models
from goods.models import Goods
from users.models import UserProfile
from user_operator.models import UserAddress
from datetime import datetime
from django.contrib.auth import get_user_model
user = get_user_model()




class ShoppingCard(models.Model):
    goodsname = models.ForeignKey(Goods,on_delete=models.CASCADE)
    goodsnum = models.IntegerField(default=1)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goodsname")

    def __str__(self):
        return '{}{}'.format(self.goodsname.goodsname,self.goodsnum)



class OrderInfo(models.Model):

    order_status = (
        ('1','完成'),
        ('2','待支付'),
        ('3','取消'),
        ('4','其他'),

    )

    user =models.ForeignKey(user,on_delete=models.CASCADE)
    ordersn=models.CharField(max_length=32)
    ordernum = models.IntegerField(default=1)
    goodsinfo = models.ForeignKey(Goods,on_delete=models.CASCADE)
    orderstatus = models.CharField(default='',choices=order_status,max_length=32)
    #useradd = models.ForeignKey(UserAddress,on_delete=models.CASCADE)
    addtime = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name ='订单'
        verbose_name_plural =verbose_name

    def __str__(self):
        return  self.ordersn
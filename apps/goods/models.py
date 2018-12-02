from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


class GoodsCategory(models.Model):
    goodscategory=(
        ('1','一级目录'),
        ('2','二级目录'),
        ('3','三级目录')
    )

    name = models.CharField(max_length=62)
    goodscategory_type=models.CharField(choices=goodscategory,max_length=32)
    add_time = models.DateTimeField(default=datetime.now)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, verbose_name="父类目级别",
                                        help_text="父目录",
                                        related_name="sub_cat")

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Goods(models.Model):

    goodsname = models.CharField(max_length=64)
    goodstype = models.ForeignKey(GoodsCategory,on_delete=models.CASCADE)
    goodsprice = models.FloatField(default=0)
    goodsnum = models.IntegerField(default=1)
    goodsdesc = UEditorField(width=1000, height=300,default='商品描述')
    add_time = models.DateField(default=datetime.now)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goodsname



#author_by zhuxiaoliang
#2018-11-22 上午9:11

from rest_framework import serializers
from .models import Goods,GoodsCategory

# class GoodsSerializers(serializers.Serializer):
#     goodsname = serializers.CharField(required=True,max_length=100)
#     goodsprice = serializers.FloatField(default=0)
#     goodsnum = serializers.IntegerField(default=1)
#     goodsdesc = serializers.CharField(max_length=100)

class GoodsCategorySerializes(serializers.ModelSerializer):

    class Meta:
        model = GoodsCategory
        fields = '__all__'



class GoodsSerializers(serializers.ModelSerializer):
    #goodstype = GoodsCategorySerializes()
    #goodstype = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Goods
        fields = '__all__'

class GoodsCategorySerializers3(serializers.ModelSerializer):
    #三级分类
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsCategorySerializers2(serializers.ModelSerializer):
    #二级
    sub_cat = GoodsCategorySerializers3(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsCategorySerializers1(serializers.ModelSerializer):
    #一级类别
    sub_cat = GoodsCategorySerializers2(many=True)

    class Meta:
        model = GoodsCategory
        fields = '__all__'

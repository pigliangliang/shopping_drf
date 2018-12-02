#author_by zhuxiaoliang
#2018-11-30 下午10:13

from rest_framework import serializers
from .models import ShoppingCard,OrderInfo
from goods.models import Goods
# class ShoppingCardSerializers(serializers.ModelSerializer):
#
#     class Meta:
#         model = ShoppingCard
#         fields = '__all__'


class ShoopingCardSerializers(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    goodsnum = serializers.IntegerField(required=True,min_value=1,
                                        error_messages={
                                            "min_value": "商品数量不能小于一",
                                            "required": "请选择购买数量"
                                        })

    goodsname = serializers.PrimaryKeyRelatedField(required=True,queryset=Goods.objects.all())

    def create(self, validated_data):
        user = self.context['request'].user
        goodsnum = validated_data['goodsnum']
        goods = validated_data['goodsname']

        existed = ShoppingCard.objects.filter(user=user,goodsname=goods)

        if existed:
            existed = existed[0]
            existed.goodsnum += goodsnum
            existed.save()
        else:
            existed = ShoppingCard.objects.create(**validated_data)

        return existed

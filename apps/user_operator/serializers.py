#author_by zhuxiaoliang
#2018-11-30 上午10:46

from .models import UserAddress,UserFav,UserMessage

from rest_framework import serializers


class UserFavSerializers(serializers.ModelSerializer):



    class Meta:
        model = UserFav
        fields  = "__all__"

class UserMessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserMessage
        fields = '__all__'


class UserAddressSerializers(serializers.ModelSerializer):

    class Meta:
        model = UserAddress
        fields = '__all__'
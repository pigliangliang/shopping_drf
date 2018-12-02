#author_by zhuxiaoliang
#2018-11-30 下午2:09

from .models import UserProfile
from rest_framework.serializers import  ModelSerializer

class UserDetailSerializers(ModelSerializer):

    class Meta:
        model = UserProfile

        fields = ['name','sex','email','mobil']
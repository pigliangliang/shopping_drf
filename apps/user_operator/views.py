from django.shortcuts import render

# Create your views here.

from  .serializers import  UserFavSerializers,UserMessageSerializers,UserAddressSerializers
from .models import UserFav,UserMessage,UserAddress

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly



class UserFavViewsets(viewsets.ModelViewSet):

    queryset =  UserFav.objects.all()
    serializer_class =  UserFavSerializers
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)
    #lookup_field = 'id'

    def get_queryset(self):
        # 只能查看当前登录用户的收藏，不会获取所有用户的收藏
        return UserFav.objects.filter(user=self.request.user)

class UserMessageViewSets(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserMessage.objects.filter(user=self.request.user)


class UserAddressViewSets(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = UserAddressSerializers
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
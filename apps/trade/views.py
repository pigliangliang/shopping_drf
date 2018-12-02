from django.shortcuts import render

# Create your views here.
from  rest_framework.viewsets import ModelViewSet
from .serializers import ShoopingCardSerializers
from .models import ShoppingCard
from rest_framework import permissions
from utils.permissions import IsOwnerOrReadOnly


class ShoppingCardViewsets(ModelViewSet):
    #queryset = ShoppingCard.objects.all()
    serializer_class = ShoopingCardSerializers
    permission_classes = (permissions.IsAuthenticated,IsOwnerOrReadOnly,)

    def get_queryset(self):
        return ShoppingCard.objects.filter(user=self.request.user)
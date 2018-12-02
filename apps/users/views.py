from django.shortcuts import render

# Create your views here.


from .models import UserProfile
from .serializers import UserDetailSerializers
from rest_framework import viewsets



class UserDetailViewset(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserDetailSerializers

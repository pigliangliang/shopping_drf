#! -*-utf:8 -*-

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.generic import View
from .models import Goods,GoodsCategory
# Create your views here.
import json
from django.forms import model_to_dict

from .serializers import GoodsSerializers,GoodsCategorySerializers1
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets

from .filters import GoodsFilters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import filters






#方式一： django CBV
"""
class GoodsListView(View):

    def get(self,request):
        goodslist=[]
        goods = Goods.objects.all()
        for good in goods:
            pass
            #方式一
            
            # g ={}
            # g['type']=good.goodsname
            # g['price']=good.goodsprice
            # g['desc']=good.goodsdesc
            # goodslist.append(g)
            

            #方式二 序列话部分字段 有些字段报错： Object of type 'date' is not JSON serializable

            # g = model_to_dict(good)
            # goodslist.append(g)

            #方法三：serializers方式
        data =serializers.serialize('json',goods)

        #return HttpResponse(json.dumps(goodslist),content_type='application/json')
        return JsonResponse(data,safe=False)
            
            
"""

#rest api view

#方式二：APIView
"""
class GoodsListView(APIView):

    def get(self,request):
        goods = Goods.objects.all()
        goods_serializers = GoodsSerializers(goods,many=True)

        return Response(goods_serializers.data)
"""

#方式三：mixin 和generics.generic.APIView
"""
class GoodsListView(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):



    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    # def post(self,request,*args,**kwargs):
    #     return self.post(request,*args,**kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
"""


#方式四：直接继承generic,无需重写get，post等方法
"""

class GoodsListView(generics.ListCreateAPIView):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
"""

# 方式五：viewset



class GoodsListView(viewsets.ModelViewSet):
    """
    配合router使用
    from rest_framework.routers import DefaultRouter

    router = DefaultRouter()
    router.register(r'goods',GoodsListView)
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializers
    filter_backends = (DjangoFilterBackend,)
    #
    filter_class = GoodsFilters
    #ordering 报错
    #ordering = ('pricenum')

class GoodsCategoryView(viewsets.ReadOnlyModelViewSet):
    authentication_classes = []
    queryset = GoodsCategory.objects.all()
    serializer_class = GoodsCategorySerializers1

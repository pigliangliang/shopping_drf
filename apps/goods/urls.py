#author_by zhuxiaoliang
#2018-11-22 上午8:47

from django.urls import path,re_path,include
from .views import GoodsListView,GoodsCategoryView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'goods',GoodsListView)
router.register(r'goodscategory',GoodsCategoryView)

app_name = 'goods'

urlpatterns = [
    path('',include(router.urls))
    #path(r'goodslist/',GoodsListView.as_view(),name='googslist'),
]
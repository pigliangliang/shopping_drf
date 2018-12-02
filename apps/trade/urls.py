#author_by zhuxiaoliang
#2018-12-01 上午9:30

from django.urls import path,re_path,include

from rest_framework.routers import DefaultRouter
from .views import ShoppingCardViewsets



router = DefaultRouter()
router.register('shoppingcard',ShoppingCardViewsets,base_name='shoppingcard')


app_name = 'trade'


urlpatterns = [
    path('',include(router.urls)),
]
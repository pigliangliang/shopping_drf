#author_by zhuxiaoliang
#2018-11-30 上午10:52


from django.urls import path,include
from .views import UserFavViewsets,UserMessageViewSets,UserAddressViewSets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('userfav',UserFavViewsets),
router.register('usermessage',UserMessageViewSets)
router.register('useraddress',UserAddressViewSets)


app_name='user_operation'


urlpatterns = [
    path('',include(router.urls))
]
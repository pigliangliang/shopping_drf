#author_by zhuxiaoliang
#2018-11-30 下午2:15


from rest_framework.routers import DefaultRouter
from .views import UserDetailViewset

from django.urls import path,include

router = DefaultRouter()
router.register('users',UserDetailViewset)

app_name = 'users'

urlpatterns =[

    path('userdetail/',include(router.urls))

]
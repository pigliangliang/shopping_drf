"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
import xadmin
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title="沐夕漫黎")


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('admin/', xadmin.site.urls),
    path('ueditor/',include('DjangoUeditor.urls')),
    path(r'goods/',include('goods.urls',namespace='goods')),
    path(r'user_operation/',include('user_operator.urls',namespace='user_operation')),
    path('api-auth/', include('rest_framework.urls',)),
    path('',include_docs_urls(title='沐夕漫黎')),
    #path('',schema_view),
    path('users/',include('users.urls',namespace='users')),
    path('trade/',include('trade.urls',namespace='trade'))

]

#author_by zhuxiaoliang
#2018-11-21 下午10:14

import xadmin

from xadmin import views


# users/adminx.py
__author__ = 'derek'

import xadmin
from xadmin import views
from users.models import UserProfile



class BaseSetting(object):
    #添加主题功能
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    #全局配置，后台管理标题和页脚
    site_title = "每日鲜果"
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    #菜单收缩
    menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['name', 'sex', "email",'mobil']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
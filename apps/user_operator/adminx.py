#author_by zhuxiaoliang
#2018-11-21 下午11:24

import xadmin

from .models import UserAddress,UserFav,UserMessage

class UserAddressAdmin(object):
    list_display = [
        'province','city','street','signer','mobile'
    ]


class UserFavAdmin(object):
    list_display = [
        'goods','user','addtime'
    ]


class UserMessageAdmin(object):
    list_display= [
        'message','add_time','goods','user'
    ]

xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFav,UserFavAdmin)
xadmin.site.register(UserAddress,UserAddressAdmin)
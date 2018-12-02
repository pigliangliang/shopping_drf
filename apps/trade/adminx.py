#author_by zhuxiaoliang
#2018-11-21 下午10:48

import xadmin

from .models import OrderInfo,ShoppingCard

class OrderInfoAdmin(object):
    list_display = [
        'ordersn','ordernum','orderstatus','user','goodsinfo'

    ]


class ShoppingCardAdmin(object):
    list_display=[
        'goodsnum','add_time','goodsname','user'
    ]

xadmin.site.register(OrderInfo,OrderInfoAdmin)
xadmin.site.register(ShoppingCard,ShoppingCardAdmin)
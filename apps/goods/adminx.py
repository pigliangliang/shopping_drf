#author_by zhuxiaoliang
#2018-11-21 下午10:33

import xadmin

from .models import Goods,GoodsCategory

class GoodAdmin(object):
    list_display=[
        'goodsname','goodsprice','goodsnum','goodsdesc'
    ]
    style_fields = {"goods_desc": "ueditor"}

class GoodsCategoryAdmin(object):
    list_display=[
        'name','goodscategory_type','add_time','parent_category'
    ]

xadmin.site.register(Goods,GoodAdmin)
xadmin.site.register(GoodsCategory,GoodsCategoryAdmin)
#author_by zhuxiaoliang
#2018-11-22 下午3:06
import django_filters
from .models import Goods

class GoodsFilters(django_filters.rest_framework.FilterSet):
    price_min = django_filters.NumberFilter(field_name='goodsprice',lookup_expr='gte',)
    price_max = django_filters.NumberFilter(field_name='goodsprice',lookup_expr='lte')

    class Meta:
        model = Goods
        fields = [
            'price_min','price_max',
        ]
from .models	import Restaurant,Menu_item
from django_filters import rest_framework as filters
from django_filters import CharFilter
from django.db import models


class RestaurantFilter(filters.FilterSet):
    class Meta:
        model = Restaurant
        fields = ['created_at','updated_at','active',
        'name','rating','status',
        'places']	
        
class MenuItemFilter(filters.FilterSet):
    class Meta:
        model = Menu_item
        fields = '__all__'	
        filter_overrides = {
            models.FileField: {
                'filter_class': CharFilter,
                'extra': lambda f: {'lookup_expr': 'exact'},
            },
        }

from .models	import Profile
from django_filters import rest_framework as filters

class ProfileFilter(filters.FilterSet):
    class Meta:
        model = Profile
        fields = ['phone','default_address',
        'updated_at','typology','user__first_name','user__last_name',
        'user__email','user__is_active','user__date_joined','restaurant']	

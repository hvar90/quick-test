"""quicktest URL Configuration

"""
from django.contrib import admin
from django.urls import include,path
from users.models import Profile
from restaurants.models import Restaurant,Menu_item,Place
from orders.models import Order,Delivery
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiV1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apiV1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('apiV1/restaurants/', include('restaurants.urls')),
    path('apiV1/users/', include('users.urls')),
    
]

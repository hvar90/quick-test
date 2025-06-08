"""quicktest URL Configuration

"""
from rest_framework.schemas import get_schema_view
from django.contrib import admin
from django.urls import include,path
from users.models import Profile
from restaurants.models import Restaurant,Menu_item,Place
from orders.models import Order,Delivery
#from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


#schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('apiv1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('apiv1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('apiv1/restaurants/', include('restaurants.urls')),
    path('apiv1/users/', include('users.urls')),    
    path('apiv1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path(
        # "openapi",
        # get_schema_view(title="Your Project", description="API for all things …"),
        # name="openapi-schema",
    # ),
	#url(r'^$', schema_view)
]

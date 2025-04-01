"""quicktest URL Configuration

"""
from .import views
from django.urls import path

urlpatterns = [
    path('', views.RestaurantList.as_view(),
     name='list_restaurants'),
    path('detail/<str:pk>/', views.restaurantDetail,name="detail"),
    path('create', views.restaurantCreate,name="create"),
    path('update/<str:pk>/', views.restaurantUpdate,name="update"),
    path('delete/<str:pk>/', views.restaurantDelete,name="delete"),
    path('menu_item', views.MenuItemList.as_view(),
     name='list_restaurants'),
    path('menu_item/detail/<str:pk>/', views.menuItemDetail,name="detail"),
    path('menu_item/create', views.menuItemCreate,name="create"),
    path('menu_item/update/<str:pk>/', views.menuItemUpdate,name="update"),
    path('menu_item/delete/<str:pk>/', views.menuItemDelete,name="delete"),
    
]

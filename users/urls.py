"""quicktest URL Configuration

"""
from .import views
from django.urls import path

urlpatterns = [
	path('', views.UserList.as_view(),
     name='list_users'),
    path('detail/<str:pk>/', views.userDetail,name="detail"),
    path('create/', views.userCreate,name="create"),
    path('update/<str:pk>/', views.userUpdate,name="update"),
    path('delete/<str:pk>/', views.userDelete,name="delete"),
    path('change_password/<int:id>/', views.ChangePassword.as_view(),
     name='change_password'),
]

"""quicktest URL Configuration

"""
from .import views
from django.urls import path

urlpatterns = [
	path('', views.UserList.as_view(),
     name='list_users'),
    path('detail/<str:pk>/', views.userDetail,name="detail"),
    path('create/', views.UserCreate.as_view(),name="create"),
    path('update/<int:pk>/', views.UserUpdate.as_view(),name="update"),
    path('delete/<str:pk>/', views.userDelete,name="delete"),
    path('upload_user/', views.UploadUser.as_view(), name='upload'),
    path('change_password/<int:id>/', views.ChangePassword.as_view(),
     name='change_password'),
]

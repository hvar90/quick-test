from .models	import Profile	
from restaurants.serializers	import RestaurantSerializer
from rest_framework import serializers
from django.contrib.auth.models	import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','is_active',
		'date_joined']


class ProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	restaurant = RestaurantSerializer(many=True, read_only=True)
	class Meta:
		model = Profile 
		fields = '__all__'
		
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
		




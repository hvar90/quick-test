from .models	import Profile, User
from restaurants.serializers	import RestaurantSerializer
from rest_framework import serializers
from django.db.models import Model
#from django.contrib.auth.models	import User

# class ProfileSerializer2(serializers.ModelSerializer):
	# restaurant = RestaurantSerializer(many=True, read_only=True)
	# class Meta:
		# model = Profile 
		# fields = '__all__'

# class UserSerializer2(serializers.ModelSerializer):
	# profile = ProfileSerializer2(many=False, read_only=False)
	# class Meta:
		# model = User
		# fields = ['first_name','last_name','email','is_active',
		# 'date_joined','profile','username']
		
	# def create(self, validated_data):
		# print(validated_data)
		# user_data = validated_data.pop('profile')
		# user_instance = User.objects.create(**user_data)
		# profile_instance = Profile.objects.create(user=user_instance, **validated_data)
		# return user_instance
		
	# def update(self, instance, validated_data):
		# profile_data = validated_data.pop('profile')
		# profile_instance = instance.profile

		# for key, value in validated_data.items():
		  # setattr(instance, key, value)
		# instance.save()

		# for key, value in profile_data.items():
		  # setattr(profile_instance, key, value)
		# profile_instance.save()

		# return instance
		

#books: List[BookSerializer] = BookSerializer(many=True, read_only=True, source='book_set')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name','last_name','email','is_active',
		'date_joined','username']

#https://www.django-rest-framework.org/api-guide/serializers/
class ProfileSerializer(serializers.ModelSerializer):
	#read only debe ser True solo en GET 
	user: User = UserSerializer(many=False, read_only=False)
	#restaurant = RestaurantSerializer(many=True, read_only=False)
	class Meta:
		model: Model = Profile 
		fields = ['user','phone','default_address','typology',]
		
	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user_instance = User.objects.create(**user_data)
		profile_instance = Profile.objects.create(user=user_instance, **validated_data)
		return profile_instance
		
	def update(self, instance, validated_data):
		user_data = validated_data.pop('user')
		user_instance = instance.user

		for key, value in validated_data.items():
		  setattr(instance, key, value)
		instance.save()

		for key, value in user_data.items():
		  setattr(user_instance, key, value)
		user_instance.save()

		return instance
		
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
class UploadUserSerializer(serializers.Serializer):
    file = serializers.FileField()
		




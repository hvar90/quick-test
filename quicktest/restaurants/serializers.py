from .models	import Restaurant,Place,Menu_item
from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
	places = PlaceSerializer(many=True, read_only=True)
	class Meta:
		model = Restaurant
		fields = '__all__'
		
class MenuItemItemSerializer(serializers.ModelSerializer):
	restaurant = RestaurantSerializer(many=False, read_only=True)
	class Meta:
		model = Menu_item
		fields = '__all__'


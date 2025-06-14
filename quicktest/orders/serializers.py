from .models	import Order,Delivery,Order_item
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['__all__']

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['__all__']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_item
        fields = ['__all__']

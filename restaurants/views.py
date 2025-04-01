from rest_framework.response import Response
from rest_framework import generics
from .filters import RestaurantFilter,MenuItemFilter
from .models import Restaurant,Place,Menu_item
from .serializers import RestaurantSerializer,MenuItemItemSerializer
from core.decorators import counter,timeit
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import (
	authentication_classes, 
	permission_classes)
	    	
class RestaurantList(generics.ListAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	model = Restaurant
	serializer_class = RestaurantSerializer	
	filterset_class = RestaurantFilter
	@counter
	@timeit
	def get_queryset(self):
		return Restaurant.objects.all()

@counter
@timeit	
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def restaurantDetail(request,pk):
	restaurant = Restaurant.object.get(id=pk)
	serializer= RestaurantSerializer(restaurant, many=False)
	return Response(serializer.data)

@counter
@timeit		
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def restaurantCreate(request):
	serializer=RestaurantSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@counter
@timeit		
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def restaurantUpdate (request,pk):
	restaurant = Restaurant.object.get(id=pk)
	serializer=RestaurantSerializer(instace=restaurant,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@counter
@timeit		
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def restaurantDelete(request,pk):
	menuItem = Restaurant.object.get(id=pk)
	restaurant.delete()
	return Response('Deleted')
	
class MenuItemList(generics.ListAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	model = Menu_item
	serializer_class = MenuItemItemSerializer	
	filterset_class = MenuItemFilter
	@counter
	@timeit
	def get_queryset(self):
		return Menu_item.objects.all()
	

@counter
@timeit		
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def menuItemDetail(request,pk):
	menuItem = Menu_item.object.get(id=pk)
	serializer= MenuItemItemSerializer(menuItem, many=False)
	return Response(serializer.data)

@counter
@timeit		
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def menuItemCreate(request):
	serializer=MenuItemItemSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@counter
@timeit		
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def menuItemUpdate (request,pk):
	menuItem = Menu_item.object.get(id=pk)
	serializer=MenuItemItemSerializer(instace=menuItem,data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@counter
@timeit		
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def menuItemDelete(request,pk):
	menuItem = Menu_item.object.get(id=pk)
	menuItem.delete()
	return Response('Deleted')
	

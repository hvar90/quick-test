# import os,sys
# sys.path.append("/Users/hvar/gitquictest/quicktest")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quicktest")
# import django
# django.setup()

import os,sys
import pandas as pd
import mimetypes
from injector import inject
from rest_framework import status
from django.db import connection 
from django.http import HttpResponse,FileResponse
from django.db.models import Count,Sum
from django.conf import settings
from wsgiref.util import FileWrapper
from django.core.files.storage import default_storage
from django.core.files.temp import NamedTemporaryFile
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import views
from restaurants.filters import RestaurantFilter,MenuItemFilter
from .models import Restaurant,Place,Menu_item
from .serializers import RestaurantSerializer,MenuItemItemSerializer
from core.decorators import counter,timeit
from core.utils import get_df_from_query,QueryService
from rest_framework.decorators import api_view
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import (
	authentication_classes, 
	permission_classes)
	

# class RestaurantList(views.APIView):
	
	# @inject
	# def __init__(self, model: Restaurant=None,
	 # serializer: RestaurantSerializer=None,
	  # filterset: RestaurantFilter=None, *args, **kwargs):
		# super().__init__(*args, **kwargs)
		# self.model = model
		# self.serializer = serializer
		# self.filterset = filterset
	# #authentication_classes = [JWTAuthentication]
	# #permission_classes = [IsAuthenticated]
	# #model = self.model
	# #serializer_class = self.serializer	
	# #queryset = Restaurant.objects.all()
	# filterset_class = RestaurantFilter
	# @counter
	# @timeit
	# def get(self, request):
		# #user = self.get_object(pk)
		# #model = self.model
		# #serializer = self.serializer
		# serializer =  self.serializer.__class__(self.model.__class__.objects.all(), many=True)
		# #filterset_class = self.filterset
		# return Response(serializer.data)
	
	# # def get_serializer_class(self):
		# # if self.request.method in ('POST', 'PUT', 'PATCH'):
			# # return self.serializer	
		# # return self.serializer	
	# # @counter
	# # @timeit
	# # def get_queryset(self):
		# # return Restaurant.objects.all()

	    	
class RestaurantList(generics.ListAPIView):
	#authentication_classes = [JWTAuthentication]
	#permission_classes = [IsAuthenticated]
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
	restaurant = Restaurant.objects.get(id=pk)
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
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	else :
		return Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 

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
	
@counter
@timeit		
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def menuItemDelete(request,pk):
	menuItem = Menu_item.object.get(id=pk)
	menuItem.delete()
	return Response('Deleted')
	
# class ReportOrdersAPIView(generics.ListAPIView):
	# #authentication_classes = [JWTAuthentication]
	# #permission_classes = [IsAuthenticated]

	# def get(self, request, month, format=None):
		# # queryset = Restaurant.objects.filter(orders__created_at__month=month).select_related("orders").annotate(
		# # num_orders=Count('orders'),
		# # total_amount_orders=Sum('orders__total_amount')).values(
		# # 'id','name', 'num_orders','total_amount_orders')
		
		# queryset = Restaurant.objects.raw("""SELECT restaurants_restaurant.id,
		 # restaurants_restaurant.name, COUNT(orders_order.delivery_id) AS num_orders,
		 # SUM(orders_order.total_amount) AS total_amount_orders FROM
		  # restaurants_restaurant INNER JOIN orders_order
		   # ON (restaurants_restaurant.id = orders_order.restaurant_id) 
		   # WHERE EXTRACT(MONTH FROM orders_order.created_at) = %s 
		   # GROUP BY restaurants_restaurant.id
		# """,[month])
		
	
		# print(queryset)
		
		
		# tmpfile = NamedTemporaryFile(dir= settings.MEDIA_ROOT,delete=True,
		 # suffix='.csv') 
		 
		# filename =tmpfile.name
		# print(filename)
		# df = pd.DataFrame.from_records(queryset)
		# df.to_csv(path_or_buf=filename, index = False)
		# #wrapper = FileWrapper(tmpfile)
		# mimetype = mimetypes.guess_type(filename)
		# print(mimetype[0])
		# response = HttpResponse(tmpfile, content_type=mimetype[0])
		# response['Content-Disposition'] = 'attachment; filename="%s"' % 'report.csv'
		# return response
		
		
class ReportOrdersAPIView(generics.ListAPIView):
	#authentication_classes = [JWTAuthentication]
	#permission_classes = [IsAuthenticated]
	
	@inject
	def __init__(self, service: QueryService, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.service = service
		

	def get(self, request, month, format=None):
		# queryset = Restaurant.objects.filter(orders__created_at__month=month).select_related("orders").annotate(
		# num_orders=Count('orders'),
		# total_amount_orders=Sum('orders__total_amount')).values(
		# 'id','name', 'num_orders','total_amount_orders')
		
		# with connection.cursor() as cursor:
			# sql_query = """SELECT restaurants_restaurant.id,
		 # restaurants_restaurant.name, COUNT(orders_order.delivery_id) AS num_orders,
		 # SUM(orders_order.total_amount) AS total_amount_orders FROM
		  # restaurants_restaurant INNER JOIN orders_order
		   # ON (restaurants_restaurant.id = orders_order.restaurant_id) 
		   # WHERE EXTRACT(MONTH FROM orders_order.created_at ) = %s 
		   # GROUP BY restaurants_restaurant.id
		# """
			# df = pd.read_sql_query(sql_query, connection,params=[month])
	
		sql_query = """SELECT restaurants_restaurant.id,
		 restaurants_restaurant.name, COUNT(orders_order.delivery_id) AS num_orders,
		 SUM(orders_order.total_amount) AS total_amount_orders FROM
		  restaurants_restaurant INNER JOIN orders_order
		   ON (restaurants_restaurant.id = orders_order.restaurant_id) 
		   WHERE EXTRACT(MONTH FROM orders_order.created_at ) = %s 
		   GROUP BY restaurants_restaurant.id
		"""
		df=self.service.get_df_from_query(sql_query,month)
		tmpfile = NamedTemporaryFile(dir= settings.MEDIA_ROOT,delete=True,
		 suffix='.csv') 
		filename =tmpfile.name
		print(filename)
		#df = pd.DataFrame.from_records(queryset)
		df.to_csv(path_or_buf=filename,sep=';',index = False)
		mimetype = mimetypes.guess_type(filename)
		response = HttpResponse(tmpfile, content_type=mimetype[0])
		response['Content-Disposition'] = 'attachment; filename="%s"' % 'report.csv'
		return response
	

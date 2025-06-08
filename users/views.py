import os
import base64
import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission
from rest_framework import generics
from rest_framework.serializers import ModelSerializer
from .filters import ProfileFilter
from .models import Profile
from .serializers import *
from .user_tasks import *
from django.db.models import Model
from celery.result import AsyncResult
from core.decorators import counter,timeit

from core.permissions import *
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import (IsAuthenticated,
								DjangoModelPermissions)
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import (
	authentication_classes, 
	permission_classes)
	
from django_filters.rest_framework import FilterSet


class UserList(generics.ListAPIView):
	#authentication_classes = [JWTAuthentication]
	#permission_classes = [IsAuthenticated]
	permission_classes: List[BasePermission] = [CustomDjangoModelPermissions]
	model: Model = Profile
	serializer_class: ModelSerializer = ProfileSerializer	
	filterset_class: FilterSet = ProfileFilter
	@counter
	@timeit
	def get_queryset(self) -> List[BasePermission]:
		return Profile.objects.all()
		
@counter
@timeit
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])	
def userDetail(request,pk) -> Response:
	user = Profile.object.get(id=pk)
	serializer= ProfileSerializer(users, many=False)
	return Response(serializer.data)

# @counter
# @timeit
# @api_view(['POST'])
# #@authentication_classes([JWTAuthentication])
# #@permission_classes([IsAuthenticated])	
# def userCreate(request):
	# serializer=ProfileSerializer(data=request.data)
	# if serializer.is_valid():
		# serializer.save()
	# return Response(serializer.data)

class UserCreate(generics.GenericAPIView):
	#permission_classes = [DjangoModelPermissions]
	serializer_class = ProfileSerializer
	#queryset=Profile.objects.all()
	@counter
	@timeit
	def post(self, request):
		serializer=ProfileSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

# @counter
# @timeit
# @api_view(['PUT'])
# #@authentication_classes([JWTAuthentication])
# #@permission_classes([IsAuthenticated])	
# @permission_classes([DjangoModelPermissions])	
# def userUpdate (request,pk):
	# user = Profile.object.get(id=pk)
	# queryset=Profile.object.get(id=pk)
	# serializer=ProfileSerializer(instace=user,data=request.data)
	# if serializer.is_valid():
		# serializer.save()
	# return Response(serializer.data)

#DjangoModelPermissions no sirve para get
class UserUpdate(generics.RetrieveUpdateAPIView):
	#permission_classes = [DjangoModelPermissions]
	serializer_class = ProfileSerializer
	queryset=Profile.objects.all()
	@counter
	@timeit
	def put(self, request, pk):
		user = Profile.object.get(id=pk)
		serializer=ProfileSerializer(instace=user,data=request.data)
		if serializer.is_valid():
			serializer.save()
		return Response(serializer.data)

@counter
@timeit
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])	
def userDelete(request,pk):
	user = Profile.object.get(id=pk)
	user.delete()
	return Response('Deleted')
	
class ChangePassword(generics.GenericAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	serializer_class = ChangePasswordSerializer
	@counter
	@timeit
	def put(self, request, id):
		password = request.data['password']
		new_password = request.data['new_password']

		obj = get_user_model().objects.get(pk=id)
		if not obj.check_password(raw_password=password):
			return Response({'error': 'password not match'}, status=400)
		else:
			obj.set_password(new_password)
			obj.save()
			return Response({'success': 'password changed successfully'},
			 status=200)

class UploadUser(generics.GenericAPIView):
	#authentication_classes = [JWTAuthentication]
	#permission_classes = [IsAuthenticated]
	serializer_class = UploadUserSerializer
	@counter
	@timeit
	def post(self, request, *args, **kwargs):
		serializer = UploadUserSerializer(data=request.data)
		if serializer.is_valid():
			file = request.FILES['file']
			file_extension = os.path.splitext(file.name)[1]
			if file_extension == ".csv":
				df = pd.read_csv(file, sep=';')
			elif file_extension == ".xlsx" or file_extension == ".xls":
				df = pd.read_excel(file, sep=';')	
			else:
				return Response({'error': f"Unsupported file type: {file_extension}"}, status=400)
				#raise ValueError(f"Unsupported file type: {file_extension}")
			if df.shape[0] > 20:
				return Response({'error': '20 new users max'}, status.HTTP_400_BAD_REQUEST)  
			df_dict = df.to_dict()
			reply=save_user_from_file.delay(df_dict)
			return  Response({"message": "Task submitted successfully!"}, status.HTTP_202_ACCEPTED)
			#reply = AsyncResult(reply.task_id).get()
			#return Response(reply[0], status=reply[1])
		else:
			return  Response(serializer.errors, status.HTTP_400_BAD_REQUEST) 
			
					 
# class UploadUser(generics.GenericAPIView):
	# #authentication_classes = [JWTAuthentication]
	# #permission_classes = [IsAuthenticated]
	# serializer_class = UploadUserSerializer
	# @counter
	# @timeit
	# def post(self, request, *args, **kwargs):
		# serializer = UploadUserSerializer(data=request.data)
		# if serializer.is_valid():
			# file = request.FILES['file']
			# file_extension = os.path.splitext(file.name)[1]
			# if file_extension == ".csv":
				# df = pd.read_csv(file, sep=';')
			# elif file_extension == ".xlsx" or file_extension == ".xls":
				# df = pd.read_excel(file, sep=';')	
			# else:
				# return Response({'error': f"Unsupported file type: {file_extension}"}, status=400)
				# #raise ValueError(f"Unsupported file type: {file_extension}")
				
			# if df.shape[0] > 20:
				# return Response({'error': '20 new users max'}, status=400)
				
				
			# for index, row in df.iterrows():
				# # data = {'default_address': row['default_address'],
				# # 'typology': row['typology'],
				# # 'phone': row['phone'],
				# # 'restaurant': [{ 'id': row['restaurant']}] ,
				 # # 'user': {'is_active': row['is_active'],
					 # # 'first_name': row['first_name'],
					 # # 'last_name': row['last_name'],
					 # # 'email': row['email'],
					 # # 'username': row['username'],
					 # # 'password': row['password'],
					 # # }}
				# data = {'default_address': row['default_address'],
				# 'typology': row['typology'],
				# 'phone': row['phone'],
				 # 'user': {'is_active': row['is_active'],
					 # 'first_name': row['first_name'],
					 # 'last_name': row['last_name'],
					 # 'email': row['email'],
					 # 'username': row['username'],
					 # 'password': row['password'],
					 # }}
				# # data = {'is_active': row['is_active'],
					 # # 'first_name': row['first_name'],
					 # # 'last_name': row['last_name'],
					 # # 'email': row['email'],
					 # # 'username': row['username'],
					 # # 'password': row['password'],
					 # # 'profile': {
						 # # 'default_address': row['default_address'],
						 # # 'typology': row['typology'],
						 # # 'phone': row['phone'],
					# # }}
				# serializer = ProfileSerializer(data=data)
				# if serializer.is_valid():
					# pass
					# #serializer.save()
				# else:
					# return Response(serializer.errors, status=400)
				
			# # profiles = [
			# # Profile(**row.to_dict()) 
				# # for index, row in df.iterrows()
			# # ]
			# # Profile.objects.bulk_create(profiles)
			# #print(df.to_dict(orient='series'))
			# # for index, row in df.iterrows():
				# # print(row.to_dict())
				# # serializer = ProfileSerializer(data=row.to_dict())
				# # if serializer.is_valid():
					# # serializer.save()
				# # else:
					# # return Response(serializer.errors, status=400)
			
			# # for record in df.to_dict(orient='records'):
				# # profile_instance = Profile(**record)
				# # profile_instance.save()
			
			
			# return Response({"message": "CSV file uploaded and processed successfully."}, status=status.HTTP_201_CREATED)
		# else:
			# return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

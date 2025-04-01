from rest_framework.response import Response
from rest_framework import generics
from .filters import ProfileFilter
from .models import Profile
from .serializers import ProfileSerializer,ChangePasswordSerializer
from core.decorators import counter,timeit
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import (
	authentication_classes, 
	permission_classes)

class UserList(generics.ListAPIView):
	authentication_classes = [JWTAuthentication]
	permission_classes = [IsAuthenticated]
	model = Profile
	serializer_class = ProfileSerializer	
	filterset_class = ProfileFilter
	@counter
	@timeit
	def get_queryset(self):
		return Profile.objects.all()
		
@counter
@timeit
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])	
def userDetail(request,pk):
	user = Profile.object.get(id=pk)
	serializer= ProfileSerializer(users, many=False)
	return Response(serializer.data)

@counter
@timeit
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])	
def userCreate(request):
	serializer=ProfileSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@counter
@timeit
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])	
def userUpdate (request,pk):
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

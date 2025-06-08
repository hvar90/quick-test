from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, force_authenticate
from django.urls import reverse
from users.models import *
from .models import *
from .views import *
from .serializers import *

class MyViewTest(TestCase):
	def setUp(self):
		Restaurant.objects.create(name="el rapidazo",rating=4.5)
		Restaurant.objects.create(name="la cocinita",rating=9.5)
		self.user = User.objects.create_user(username='doejon', password='password123',first_name='Doe')
		user_profile = Profile.objects.create(user=self.user, phone='3145649312')
		self.url_list = "/apiv1/restaurants/"
		self.url_create = "/apiv1/restaurants/create/"
		self.url_detail = "/apiv1/restaurants/detail/1/"
	def test_get_list(self):
		client = APIClient()
		client.force_authenticate(user=self.user)
		#response = client.get(reverse('list_restaurants'))
		response = client.get(self.url_list)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		expected_data =RestaurantSerializer(Restaurant.objects.all(), many=True).data
		#print(response.json()) sin pagination
		#print(response.data['results'])
		self.assertEqual(response.data['results'],expected_data)
		
		#print(len(response.context['my_objects']))
	   # print()
		#self.assertContains(response, "Hello, world!")

	def test_post_create(self):
		data = {"name": "rica comida","rating": 4.1,"status":"abierto",
				"category":"comida americana"}
		client = APIClient()
		client.force_authenticate(user=self.user)
		response = client.post(self.url_create, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data, RestaurantSerializer(Restaurant.objects.last()).data)
	  #response = self.client.post(reverse('my_view'), {'data': 'test'})
	  #self.assertEqual(response.status_code, 200)
	  # Add more assertions based on your view logic
	  
	def test_get_detail(self):
		client = APIClient()
		client.force_authenticate(user=self.user)
		response = client.get(self.url_detail)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, RestaurantSerializer(Restaurant.objects.get(id=1)).data)

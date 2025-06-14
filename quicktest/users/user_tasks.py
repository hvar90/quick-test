from celery import shared_task
from .models import Profile
from .serializers import *
from rest_framework import status
from django.db import transaction
import pandas as pd
import base64
import os

@shared_task
def save_user_from_file(df_dict):
	df = pd.DataFrame.from_dict(df_dict)
	for index, row in df.iterrows():
		data = {'default_address': row['default_address'],
		'typology': row['typology'],
		'phone': row['phone'],
		 'user': {'is_active': row['is_active'],
			 'first_name': row['first_name'],
			 'last_name': row['last_name'],
			 'email': row['email'],
			 'username': row['username'],
			 'password': row['password'],
			 }}
	serializer = ProfileSerializer(data=data)
	with transaction.atomic():
		try:
			if serializer.is_valid():
				#serializer.save()
				return  ({"message": "CSV file uploaded and processed successfully."}, status.HTTP_201_CREATED)  
			else:
				return  (serializer.errors, status.HTTP_400_BAD_REQUEST) 
		except Exception:
			# Handle the case where the instance does not exist
			pass
	
	
	
	
	


		
		
		

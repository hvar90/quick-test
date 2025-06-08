from django.db import models 
from django.db.models import Model
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from typing import Tuple
import datetime

#from django.contrib.auth.models	import User

class User(AbstractUser):
	
	def save(self, *args, **kwargs) -> None:
		# Custom logic before saving
		if not self.password.startswith('pbkdf2_sha256$'):
			self.password = make_password(self.password)  
		super().save(*args, **kwargs)
	
	# def save(self):
		# user = super(User, self)
		# user.set_password(self.password)
		# user.save()
		# return user

	def __str__(self):
		return self.username

class Profile(Model):
	class Typology(models.TextChoices):
		DEALER: Tuple[str, str] = "de", "dealer"
		CUSTOMER: Tuple[str, str]= "cu", "customer"
	user: Model = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,related_name='profile'
	)
	phone: str = models.CharField(max_length=20)
	default_address: str = models.TextField()
	updated_at: datetime = models.DateField(auto_now=True)
	typology: str =models.CharField(max_length=10, choices=Typology.choices,
		default=Typology.CUSTOMER)
	restaurant: Model = models.ManyToManyField("restaurants.Restaurant")
	
	def __str__(self) -> str:
		return str(self.user)
	

   

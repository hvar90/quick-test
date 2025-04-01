from django.db import models
from django.contrib.auth.models	import User

class Profile(models.Model):
	class Typology(models.TextChoices):
		DEALER = "de", "dealer"
		CUSTOMER = "cu", "customer"
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	phone = models.CharField(max_length=20)
	default_address = models.TextField()
	updated_at = models.DateField(auto_now=True)
	typology =models.CharField(max_length=10, choices=Typology.choices,
		default=Typology.CUSTOMER)
	restaurant = models.ManyToManyField("restaurants.Restaurant")
	
	def __str__(self):
		return str(self.user)
	

   

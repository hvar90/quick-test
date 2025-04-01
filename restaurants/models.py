from django.db import models

class Restaurant(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,db_index=True)
	updated_at = models.DateTimeField(auto_now=True,db_index=True)
	active = models.BooleanField(default=False)
	name = models.CharField(max_length=255)
	rating = models.DecimalField(max_digits=5,decimal_places=2)
	status = models.CharField(max_length=20)
	category = models.CharField(max_length=100)
	
	def __str__(self):
		return self.name

class Place(models.Model):
	address = models.TextField()
	latitude = models.DecimalField(max_digits=21,decimal_places=11)
	longitude = models.DecimalField(max_digits=21,decimal_places=11)
	restaurant = models.ForeignKey(Restaurant,related_name='places',
	 on_delete=models.CASCADE)
	
	def __str__(self):
		return self.address
	
class Menu_item(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,db_index=True)
	updated_at = models.DateTimeField(auto_now=True,db_index=True)
	active = models.BooleanField(default=False)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=10,decimal_places=2)
	preparation_time = models.IntegerField()
	available = models.BooleanField(default=False)
	category = models.CharField(max_length=100)
	# file will be uploaded to MEDIA_ROOT/uploads
	image_url = models.FileField(upload_to="uploads/")
	
	def __str__(self):
		return self.name


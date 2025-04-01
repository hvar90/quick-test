from django.db import models

class Delivery(models.Model):
	address = models.TextField()
	special_instructions = models.TextField()
	estimated_time = models.DateTimeField()
	
	def __str__(self):
		return self.address

class Order(models.Model):
	delivery = models.OneToOneField(
		Delivery,
		on_delete=models.CASCADE,
		primary_key=True,
	)
	created_at = models.DateTimeField(auto_now_add=True,db_index=True)
	updated_at = models.DateTimeField(auto_now=True,db_index=True)
	active = models.BooleanField(default=False)
	customer = models.ForeignKey("users.Profile",
	 on_delete=models.CASCADE)
	restaurant = models.ForeignKey("restaurants.Restaurant",
	 on_delete=models.CASCADE)
	status = models.CharField(max_length=20)
	total_amount = models.DecimalField(max_digits=10,decimal_places=2)
	
	def __str__(self):
		return str(self.delivery)
		
class Order_item(models.Model):
	created_at = models.DateTimeField(auto_now_add=True,db_index=True)
	updated_at = models.DateTimeField(auto_now=True,db_index=True)
	active = models.BooleanField(default=False)
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	menu_item = models.ForeignKey("restaurants.Menu_item",
	 on_delete=models.CASCADE)
	quantity = models.IntegerField()
	total_amount = models.DecimalField(max_digits=10,decimal_places=2)
	notes = models.TextField()
	
	def __str__(self):
		return str(self.order)
	
	

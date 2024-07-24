from django.db import models

class PizzaOrder(models.Model):
	PIZZA_CHOICES = [
		('margherita', 'Margherita'),
		('pepperoni', 'Pepperoni'),
		('vegetarian', 'Vegetarian'),
		# Add more pizza types as needed
	]

	pizza_type = models.CharField(max_length=50, choices=PIZZA_CHOICES)
	comments = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.pizza_type} - {self.created_at}"
from django import forms

class PizzaOrderForm(forms.Form):
	PIZZA_CHOICES = [
		('margherita', 'Margherita'),
		('pepperoni', 'Pepperoni'),
		('vegetarian', 'Vegetarian'),
		# Add more pizza types as needed
	]
	
	pizza_type = forms.ChoiceField(choices=PIZZA_CHOICES, label='Type of Pizza')
	comments = forms.CharField(widget=forms.Textarea, label='Comments or Special Instructions', required=False)
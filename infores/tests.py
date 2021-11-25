from django.test import TestCase
from .models import *

class RestaurantModelTests(TestCase):
	def test_restaurant_name(self):
		new_restaurant = Job(name='Enroute Rest')
		print(new_restaurant)
		self.assertIs(str(new_restaurant), 'Enroute Rest')
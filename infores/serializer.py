from rest_framework import serializers
from .models import Direction
from .models import Restaurant
# Create a model serializer 
class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer()
    # specify model and fields
    class Meta:
        model = Restaurant
        fields = '__all__'



from rest_framework import serializers
from .models import Product
 


class ProductSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Product
        fields = '__all__'


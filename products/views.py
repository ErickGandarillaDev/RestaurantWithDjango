from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .serializer import ProductSerializer
from .models import Product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
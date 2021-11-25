from rest_framework import viewsets
  
# import local data
from .serializer import DirectionSerializer
from .serializer import RestaurantSerializer

from .models import Direction
from .models import Restaurant


class DirectionViewSet(viewsets.ModelViewSet):
    queryset= Direction.objects.all()
    serializer_class = DirectionSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
# import local data
from .serializer import StatusSerializer
from .serializer import OrderSerializer
from .serializer import ProductDetailSerializer


from .models import Status
from .models import Order
from .models import ProductDetail




class StatusViewSet(ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

  
# create a viewset
class OrderViewSet(ModelViewSet):
    # define queryset
    queryset = Order.objects.all()
      
    # specify serializer to be used
    serializer_class = OrderSerializer





class ProductDetailViewSet(ModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailSerializer



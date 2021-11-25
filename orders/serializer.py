from rest_framework import serializers
from .models import Status
from .models import Order
from .models import ProductDetail
from products.serializer import ProductSerializer

# Create a model serializer 
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    # specify model and field
    #product = ProductSerializer();
    class Meta:
        model = ProductDetail
        fields = '__all__'






class OrderSerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True);
    #products = ProductDetailSerializer(many=True);
    status= StatusSerializer()

    # specify model and fields
    class Meta:
        model = Order
        fields = '__all__'


class RefreshTokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    # access = serializers.CharField()

    default_error_messages = {
        'bad_token': ('Token is invalid or expired')
    }

    def validate(self, attrs):
        print(attrs)
        self.refresh_token = attrs['refresh']
        # self.access_token = attrs['access']
        return attrs

    def save(self, **kwargs):
        try:
            # AccessToken(self.access_token).blacklist()
            RefreshToken(self.refresh_token).blacklist()
        except TokenError:
            self.fail('bad_token')


from django.db.models import fields
from rest_framework import serializers
from .models import Order, Brand, Type

class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Order
        fields = "__all__"

class  TypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        
class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class All_serializers(serializers.ModelSerializer):
    orders = serializers.SerializerMethodField()
    types = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()
    
    
    def get_orders(self, obj):
        orders = obj.order_set.all()
        serializer = OrderSerializers(orders, many=True)
        return serializer.data

    def get_types(self, obj):
        types = obj.type_car_set.all()
        serializer = TypeSerializers(types, many=True, read_only=True)  
        return serializer.data

    def get_brands(self, obj):
        brands = obj.brand_car_set.all()
        serializer = BrandSerializers(brands, many=True, read_only=True)  
        return serializer.data
    
    class Meta:
        model = Order
        fields = ('id', 'date', 'color_car_id', 'type_car_id')
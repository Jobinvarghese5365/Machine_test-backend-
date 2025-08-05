# products/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

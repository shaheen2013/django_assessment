from rest_framework import serializers

from product.models import Product, ProductVariant


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'status', 'price', 'image', 'product_class')
        extra_kwargs = {
            'price': {'write_only': True},
            'image': {'write_only': True},
            'product_class': {'write_only': True},
        }


class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ('title', 'available_stock')


class ProductDetailsSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, source='productvariant_set', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'product_class', 'price', 'image', 'status', 'variants')

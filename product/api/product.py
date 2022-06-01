import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, mixins, filters
from rest_framework.response import Response

from product.models import Product
from product.serializers.product import ProductListSerializer, ProductDetailsSerializer


class ProductFilter:
    pass


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'product_class', 'status']

    def post(self, request, *args, **kwargs):
        super(ProductList, self).post(request, *args, **kwargs)
        return Response({'status': True})


class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        super(ProductDetails, self).put(request, *args, **kwargs)
        return Response({'status': True})

    def delete(self, request, *args, **kwargs):
        super(ProductDetails, self).delete(request, *args, **kwargs)
        return Response({'status': True})

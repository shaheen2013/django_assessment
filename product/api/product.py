from rest_framework import generics, mixins
from rest_framework.response import Response

from product.models import Product
from product.serializers.product import ProductListSerializer, ProductDetailsSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

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

from django.urls import path

from product.api.product import ProductList, ProductDetails

urlpatterns = [
    path('products/', ProductList.as_view()),
    path('product/<int:id>/', ProductDetails.as_view()),
]

from django.contrib import admin

# Register your models here.
from product.models import Product, ProductVariant


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductVariantInline,)
    list_display = ('name', 'product_class', 'price', 'status')

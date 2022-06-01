from django.db import models

PRODUCT_STATUS_CHOICE = (
    ('available', 'available'),
    ('unavailable', 'unavailable"'),
)


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    product_class = models.CharField(max_length=200, verbose_name='class')
    price = models.FloatField()
    status = models.CharField(choices=PRODUCT_STATUS_CHOICE, max_length=200)
    image = models.ImageField(null=True)


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    available_stock = models.FloatField()

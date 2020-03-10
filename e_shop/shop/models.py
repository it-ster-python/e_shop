from django.db import models


class DressSize(models.Model):
    asian_sizes = [
        "S", "M", "L", "XL", "XXL", "3XL", "4XL", "5XL", "6XL", "7XL"
    ]
    name = models.CharField(max_length=25, verbose_name="Size name.")
    asia = models.CharField(max_length=3, choices=asian_sizes)


class Product(models.Model):
    
    name = models.CharField(max_length=75, verbose_name="Product name.")
    price = models.FloatField(verbose_name="Product price.")
    description = models.TextField(verbose_name="Product description.")
    # size = 

    class Meta:
        db_table = "products"
        verbose_name = "Product for shop."

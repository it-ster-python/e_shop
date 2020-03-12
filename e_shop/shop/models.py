from django.core.exceptions import ValidationError
from django.db import models


def rus_size_valid(value):
    sizes = (40, 42, 44, 46, 48, 50, 52, 54, 56)
    if value not in sizes:
        raise ValidationError(
            "Russian size invalid. Must be in '{}'".format(sizes)
        )


class DressSize(models.Model):
    asian_sizes = [
        "S",
        "M",
        "L",
        "XL",
        "XXL",
        "3XL",
        "4XL",
        "5XL",
        "6XL",
        "7XL",
    ]
    name = models.CharField(max_length=25, verbose_name="Size name.")
    asia = models.CharField(
        max_length=3, choices=asian_sizes, verbose_name="Asia size."
    )
    russia = models.SmallIntField(
        validators=[rus_size_valid], verbose_name="Russia size."
    )


class Product(models.Model):

    name = models.CharField(max_length=75, verbose_name="Product name.")
    price = models.FloatField(verbose_name="Product price.")
    description = models.TextField(verbose_name="Product description.")
    # size =

    class Meta:
        db_table = "products"
        verbose_name = "Product for shop."

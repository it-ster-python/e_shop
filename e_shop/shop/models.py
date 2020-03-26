import os
from django.core.exceptions import ValidationError
from django.db import models
from time import strftime

<<<<<<< HEAD

def rus_size_valid(value):
    sizes = [40, 42, 44, 46, 48, 50, 52, 54, 56]
    if value not in sizes:
        raise ValidationError(
            "Russia size invalid. Must be in '{}'".format(sizes))


def price_valid(value):
    if value < 0.01:
        raise ValidationError(f"Price '{value}' very small.")


def sale_price(value):
    if 0 < value > 100:
        raise ValidationError(f"Sale '{value}' invalid ")

=======
def rus_size_valid(value):
    sizes = [40, 42, 44, 46, 48, 50, 52, 54, 56]
    if value not in sizes:
        raise ValidationError("Russia size invalid. Must be in '{}'".format(sizes))

def price_valid(value):
    if value <0.01:
        raise ValidationError(f"Price '{value}' very small.")

def sale_price(value):
    if 0 < value > 100:
        raise ValidationError(f"Sale '{value}' invalid ")
>>>>>>> c4efab4b9b7fc2494af5b6ae1326c147162df497

class DressSize(models.Model):
    asian_size = [
        ["S", "Small"],
        ["S", "Small"],
        ["M", "Middle"],
        ["L", "Large"],
        ["L", "Large"],
        ["XL", "Extra Large"],
        ["XXL", "2 Extra Large"],
        ["XXL", "2 Extra Large"],
        ["3XL", "3 Extra Large"]
        ]
    internetional_size = [
        ["XXS", "2 Extra Small"],
        ["XS", "Extra Small"],
        ["S", "Small"],
        ["M", "Middle"],
        ["L", "Large"],
        ["XL", "Extra Large"],
        ["XXL", "2 Extra Large"],
        ["3XL", "3 Extra Large"],
        ["4XL", "4 Extra Large"]
        ]
    name = models.CharField(max_length=25, verbose_name="Size name.")
    asia = models.CharField(
        max_length=3, choices=asian_size, verbose_name="Asia size.")
    russia = models.SmallIntegerField(
        validators=[rus_size_valid], verbose_name="Russian size.")
    internetional = models.CharField(
        max_length=3, choices=internetional_size,
        verbose_name="Internetional size.")

    class Meta:
        db_table = "sizes"
        verbose_name = "Dress sizes"
        verbose_name_plural = "Sezes of dreses"

    def __str__(self):
        return self.name



class Product(models.Model):

    def path_upload(self, filename):
        return os.path.join(
                "products",
                strftime("%Y/%m"),
                self.name.replace(" ", "_"), filename)
    size = models.ForeignKey(
        DressSize, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=75, verbose_name="Product name.")
    price = models.FloatField(
        validators=[price_valid], verbose_name="Product price.")
    sale = models.FloatField(
        null=True, validators=[sale_price], verbose_name="Product sale.")
    description = models.TextField(verbose_name="Product description")
    count = models.PositiveSmallIntegerField(verbose_name="Counts dresses.")
    image = models.ImageField(
        upload_to=path_upload, verbose_name="Product image.")
    is_active = models.BooleanField(default=True, verbose_name="Active.")

    class Meta:
        db_table = "products"
        verbose_name = "Product for shop"
        verbose_name_plural = "Products for shop"

    def delete(self):
        try:
            os.remove(os.path.abspath(self.image))
        except Exception:
            pass

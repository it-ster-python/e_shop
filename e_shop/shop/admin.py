from django.contrib import admin
from shop import models

class AdminDressSize(admin.ModelAdmin):

    list_display = ("name", "internetional")

class AdminProduct(admin.ModelAdmin):

    list_display = (
        "name",
        "price",
        "count",
        "is_active"
    )


admin.site.register(models.DressSize, AdminDressSize)
admin.site.register(models.Product, AdminProduct)

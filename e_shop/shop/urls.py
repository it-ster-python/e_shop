from django.urls import path
from shop import views as shop

urlpatterns = [
    path("product/<int:product_id>/", shop.product, name="single_product"),
    path("products/", shop.products, name="products"),
]
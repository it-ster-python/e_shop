from django.urls import path
from shop import views as shop

urlpatterns = [
    path("product/", shop.product, name="product"),
    path("products/", shop.products, name="products"),
    # path("product/<product_id:int>/", shop.product, name="single_product"),
]

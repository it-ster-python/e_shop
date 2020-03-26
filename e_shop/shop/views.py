from django.shortcuts import render
from shop.models import Product


def products(request):
    prod = Product.objects.all()
    context = {
        "allprod": prod
    }
    return render(request, "products.html", context)


# def product(request, product_id):
def product(request):
    context = {}
    return render(request, "single_product.html", context)

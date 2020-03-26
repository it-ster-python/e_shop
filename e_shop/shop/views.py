from django.shortcuts import render
from shop.models import Product


def products(request):
    prods = Product.objects.all()
    context = {
        "allprod": prods
    }
    return render(request, "products.html", context)


# def product(request, product_id):
def product(request):
    context = {}
    return render(request, "single_product.html", context)


def shop_pages(request):
    context = {}
    return render(request, 'shop.html', context)

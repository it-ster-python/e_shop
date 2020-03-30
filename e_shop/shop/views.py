from django.shortcuts import render
from shop.models import Product

def products(request):
    prods = Product.objects.all()
    context = {
        "allprod": prods
    }
    return render(request, "products.html", context)

def product(request, product_id):
    context = {
        "product": Product.objects.get(id=product_id)  #так не делать
    }
    return render(request, "single_product.html", context)

from django.shortcuts import render


def products(request):
    context = {}
    return render(request, "products.html", context)


def product(request, product_id):
    context = {}
    return render(request, "single_product.html", context)

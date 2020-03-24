from django.shortcuts import render


def products(request):
    context = {
        "shop": [
         {
            'image': 'product-1.jpg',
            'name': 'Even the all-powerful Pointing has no control about the blind texts',
            'sale': '10',
            'price': "130",
            'price_sale': "50",
            },
         {
           'image': 'product-2.jpg',
           'name': 'Even the all-powerful Pointing has no control about the blind texts',
           'sale': '10',
           'price': "130",
           'price_sale': "50",
           },
         {
           'image': 'product-3.jpg',
           'name': 'Even the all-powerful Pointing has no control about the blind texts',
           'sale': '10',
           'price': "130",
           'price_sale': "50",
           },
         {
           'image': 'product-4.jpg',
           'name': 'Even the all-powerful Pointing has no control about the blind texts',
           'sale': '10',
           'price': "130",
           'price_sale': "50",
           },
         {
           'image': 'product-5.jpg',
           'name': 'Even the all-powerful Pointing has no control about the blind texts',
           'sale': '10',
           'price': "130",
           'price_sale': "50",
           },
        ]
    }
    return render(request, "products.html", context)


def product(request, product_id):
    context = {}
    return render(request, "single_product.html", context)


def shop_pages(request):
    context = {}
    return render(request, 'shop.html', context)

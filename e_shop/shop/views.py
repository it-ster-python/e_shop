from django.shortcuts import render

def products(request):
    context = {
        "allprod": [
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "sale": 30,
                "image": "product-1.jpg",
                "status": "30%",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-2.jpg",
                "status": "New Arrival",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-3.jpg",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "pricesale": 90,
                "image": "product-4.jpg",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-5.jpg",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-6.jpg",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-7.jpg",
            },
            {
                "name": "Young Woman Wearing Dress",
                "price": 120,
                "image": "product-8.jpg",
                "status": "Best Sellers",
            },
        ]
    }
    return render(request, "products.html", context)

# def product(request, product_id):
def product(request):
    context = {}
    return render(request, "single_product.html", context)

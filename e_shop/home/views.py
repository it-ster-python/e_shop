from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "trending": [
            {
                "name": "Young Woman Wearing Dress 1",
                "price": 120.00,
                "sale": 50,
                "image": "product-1.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 2",
                "price": 110.00,
                "image": "product-2.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 3",
                "price": 80.00,
                "image": "product-3.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 4",
                "price": 800.00,
                "sale": 60,
                "image": "product-4.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 5",
                "price": 200.00,
                "sale": 50,
                "image": "product-5.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 6",
                "price": 150.00,
                "image": "product-6.jpg"
            }
        ]
    }
    return render(request, "home.html", context)

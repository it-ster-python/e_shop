from django.shortcuts import render

# Create your views here.

def home_page(request):
    context = {
        "trending": [
            {
                "name": "Young Woman Wearing Dress 1",
                "price": 120.00,
                "sale": 39.12,
                "image": "product-1.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 2",
                "price": 110.00,
                "image": "product-2.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 3",
                "price": 190.00,
                "sale": 50,
                "image": "product-3.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 4",
                "price": 113.80,
                "image": "product-4.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 5",
                "price": 1120.00,
                "sale": 10,
                "image": "product-5.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 6",
                "price": 10.50,
                "sale": 1,
                "image": "product-6.jpg"
            },
        ],
        "products": [
            {
                "name": "Young Woman Wearing Dress 1",
                "price": 120.00,
                "image": "product-1.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 2",
                "price": 110.00,
                "image": "product-2.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 3",
                "price": 190.00,
                "image": "product-3.jpg"
            },
            {
                "name": "Young Woman Wearing Dress 4",
                "price": 113.80,
                "image": "product-4.jpg"
            },
        ],
        "testimory": [
            {
            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
            "name": "Roger Scott",
            "who": "Customer",
            "image": "person_1.jpg",
            },
            {
            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
            "name": "Roger Scott",
            "who": "Customer",
            "image": "person_2.jpg",
            },
            {
            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
            "name": "Roger Scott",
            "who": "Customer",
            "image": "person_3.jpg",
            },
            {
            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
            "name": "Roger Scott",
            "who": "Customer",
            "image": "person_1.jpg",
            },
            {
            "text": "A small river named Duden flows by their place and supplies it with the necessary regelialia. It is a paradisematic country, in which roasted parts of sentences fly into your mouth.",
            "name": "Roger Scott",
            "who": "Customer",
            "image": "person_1.jpg",
            },
        ],
        "recentblog": [
            {
                "images": "image_1.jpg",
                "text": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Dec 6, 2018",
                "author": "Admin",
                "comments": "30",
            },
            {
                "images": "image_2.jpg",
                "text": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Dec 6, 2018",
                "author": "Admin",
                "comments": "30",
            },
            {
                "images": "image_3.jpg",
                "text": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Dec 6, 2018",
                "author": "Admin",
                "comments": "30",
            },
        ],
        "services": [
            {
                "pacage": "Refund Policy",
                "text": "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic.",
            },
            {
                "pacage": "Premium Packaging",
                "text": "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic.",
            },
            {
                "pacage": "Superior Quality",
                "text": "Even the all-powerful Pointing has no control about the blind texts it is an almost unorthographic.",
            },
        ]
    }
    return render(request, "home.html", context)
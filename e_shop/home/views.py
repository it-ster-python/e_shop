from django.shortcuts import render

# Create your views here.
def home_page(request):
    context = {
        "trending": [
            {
                "name": "Young Woman Wearing Dress 1",
                "price": 120.00,
                "sale": 50,
                "image": "product-1.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 2",
                "price": 110.00,
                "image": "product-2.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 3",
                "price": 80.00,
                "image": "product-3.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 4",
                "price": 800.00,
                "sale": 60,
                "image": "product-4.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 5",
                "price": 200.00,
                "sale": 50,
                "image": "product-5.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 6",
                "price": 150.00,
                "image": "product-6.jpg",
            },
        ],
        "products": [
            {
                "name": "Young Woman Wearing Dress 1",
                "price": 120.00,
                "image": "product-1.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 2",
                "price": 120.00,
                "image": "product-2.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 3",
                "price": 120.00,
                "image": "product-3.jpg",
            },
            {
                "name": "Young Woman Wearing Dress 4",
                "price": 120.00,
                "image": "product-4.jpg",
            },
        ],
        "slider": [
            {
                "image": "person_1.jpg",
                "text": "A small river named Duden flows by their place and supplies"
                "it with the necessary regelialia. It is a paradisematic country, in"
                "which roasted parts of sentences fly into your mouth.",
                "name": "Roger Scott",
                "position": "Customer",
            },
            {
                "image": "person_2.jpg",
                "text": "A small river named Duden flows by their place and supplies"
                "it with the necessary regelialia. It is a paradisematic country, in"
                "which roasted parts of sentences fly into your mouth.",
                "name": "Roger Scott",
                "position": "Customer",
            },
            {
                "image": "person_3.jpg",
                "text": "A small river named Duden flows by their place and supplies"
                "it with the necessary regelialia. It is a paradisematic country, in"
                "which roasted parts of sentences fly into your mouth.",
                "name": "Roger Scott",
                "position": "Customer",
            },
            {
                "image": "person_2.jpg",
                "text": "A small river named Duden flows by their place and supplies"
                "it with the necessary regelialia. It is a paradisematic country, in"
                "which roasted parts of sentences fly into your mouth.",
                "name": "Roger Scott",
                "position": "Customer",
            },
            {
                "image": "person_1.jpg",
                "text": "A small river named Duden flows by their place and supplies"
                "it with the necessary regelialia. It is a paradisematic country, in"
                "which roasted parts of sentences fly into your mouth.",
                "name": "Roger Scott",
                "position": "Customer",
            },
        ],
        "blogs": [
            {
                "image": "image_1.jpg",
                "title": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Dec 6, 2018",
                "user": "Admin",
                "comments": 3,
            },
            {
                "image": "image_2.jpg",
                "title": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Mar 6, 2020",
                "user": "User",
                "comments": 4,
            },
            {
                "image": "image_3.jpg",
                "title": "Even the all-powerful Pointing has no control about the blind texts",
                "date": "Jul 6, 2019",
                "user": "Editor",
                "comments": 2,
            },
        ],
        "partners": [
            {"count": 1000, "type": "Happy Customers"},
            {"count": 20000, "type": "Branches"},
            {"count": 300, "type": "Partner"},
            {"count": 40, "type": "Awards"},
        ],
        "services": [
            {
                "name": "Refund Policy",
                "description": "Even the all-powerful Pointing has no control "
                "about the blind texts it is an almost unorthographic.",
            },
            {
                "name": "Premium Packaging",
                "description": "Even the all-powerful Pointing has no control "
                "about the blind texts it is an almost unorthographic.",
            },
            {
                "name": "Superior Quality",
                "description": "Even the all-powerful Pointing has no control "
                "about the blind texts it is an almost unorthographic.",
            },
        ],
    }
    return render(request, "home.html", context)

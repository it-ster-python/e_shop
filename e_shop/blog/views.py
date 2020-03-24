from django.shortcuts import render

def blog_page(request):
    context = {
        "blog": [
            {
            "image": "image_1.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Dec 6, 2018",
            "author": "Admin",
            "comments": "300",
            },
            {
            "image": "image_2.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Apr 31, 2018",
            "author": "Admin",
            "comments": "1",
            },
            {
            "image": "image_3.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Jul 18, 2018",
            "author": "Admin",
            "comments": "557",
            },
            {
            "image": "image_4.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "May 61, 2020",
            "author": "Admin",
            "comments": "7",
            },
            {
            "image": "image_5.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Dec 7, 2018",
            "author": "Admin",
            "comments": "0",
            },
            {
            "image": "image_6.jpg",
            "heading": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Feb 6, 2019",
            "author": "Admin",
            "comments": "10",
            },
        ]
    }
    return render(request, "blog.html", context)

def blog_single(request):
    context = {
        "blogsingle":[
            {
            "images": "image_1.jpg",
            "namenews": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "Dec 22, 2001",
            "author": "Admin",
            "comments": "0"
            },
            {
            "images": "image_2.jpg",
            "namenews": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "July 12, 2018",
            "author": "Admin",
            "comments": "19"
            },
            {
            "images": "image_3.jpg",
            "namenews": "Even the all-powerful Pointing has no control about the blind texts",
            "date": "May 30, 2028",
            "author": "Admin",
            "comments": "85"
            },
        ]
    }
    return render(request, "blog-single.html", context)
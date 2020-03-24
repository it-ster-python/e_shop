from django.shortcuts import render


def blog_page(request):
    context = {
        "blogs": [
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-1.jpg',
            },
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-2.jpg',
            },
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-3.jpg',
            },
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-4.jpg',
            },
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-5.jpg',
            },
            {
                'name': 'Even the all-powerful Pointing has no control about the blind texts',
                'access': 'admin',
                "date": 'Dec 6, 2018',
                'comment': '3',
                'image': 'product-6.jpg',
            },
        ]
    }
    return render(request, 'blog.html', context)

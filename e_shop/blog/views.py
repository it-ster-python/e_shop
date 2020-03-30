from django.shortcuts import render
from blog.models import Article

def blog_page(request):
    blogs = Article.objects.all()
    context = {
        "blog": blogs
    }
    return render(request, "blog.html", context)

def blog_single(request, article_id):
    blogpost = Article.objects.get(id=article_id)
    blogrecent = Article.objects.order_by('-add_time')[:3]
    last_comment = blogpost.comment_set.order_by('-id')[:10]
    context = {
        "blogsingle": blogpost,
        "blogrecent": blogrecent,
        "last_comment": last_comment
    }
    return render(request, "blog-single.html", context)
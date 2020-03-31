from django.shortcuts import render
from blog.models import Article
from blog.forms import CommentForm

def blog_page(request):
    blogs = Article.objects.all()
    context = {
        "blog": blogs
    }
    return render(request, "blog.html", context)

def blog_single(request, article_id):
    if request.method == "POST":
        pass
    blogpost = Article.objects.get(id=article_id)
    blogrecent = Article.objects.all().order_by('-add_time')[:3]
    last_comment = blogpost.comment.all().order_by('-id')[:10]
    comment_form = CommentForm(
        initial={
            "comment_article": blogpost
        }
    )
    context = {
        "blogsingle": blogpost,
        "blogrecent": blogrecent,
        "last_comment": last_comment,
        "comment_form": comment_form
    }
    return render(request, "blog-single.html", context)

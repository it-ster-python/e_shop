from django.shortcuts import render
from blog.models import Article
from blog.forms import CommentForm
from django.http import HttpResponseRedirect

def blog_page(request):
    blogs = Article.objects.all()
    context = {
        "blog": blogs
    }
    return render(request, "blog.html", context)

def blog_single(request, article_id):
    blogpost = Article.objects.get(id=article_id)
    blogrecent = Article.objects.all().order_by('-add_time')[:3]
    last_comment = blogpost.comment.all().order_by('-id')[:10]
    comment_form = CommentForm(
        initial={
            "comment_article": blogpost
        }
    )
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect(
                f"/blog/blogsingle/{blogpost.id}"
            )
        else:
            print("don't valid")
    context = {
        "blogsingle": blogpost,
        "blogrecent": blogrecent,
        "last_comment": last_comment,
        "comment_form": comment_form
    }
    return render(request, "blog-single.html", context)

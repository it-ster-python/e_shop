from django.shortcuts import render, get_object_or_404
from blog.models import Article


def blog_page(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'blog.html', context)


def blog_show(request, article_id):
    article = get_object_or_404(Article,  id=article_id)
    # comments = Comments.objects.filter(comments_articles=article_id)
    context = {
        "article": article,
        # 'comments': comments
    }
    return render(request, 'blog_single.html', context)

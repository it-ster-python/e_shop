from django.urls import path
from blog import views as blog

urlpatterns = [
    path("", blog.blog_page, name="blog"),
    path("<int:article_id>/", blog.blog_show, name='article')
]

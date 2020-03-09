from django.urls import path
from blog import views as blog

urlpatterns = [
    path("blogsingle", blog.blog_single, name="blogsingle"),
    path("", blog.blog_page, name="blog"),
]

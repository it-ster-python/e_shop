import os
from django.core.exceptions import ValidationError
from django.db import models
from time import strftime


class Article(models.Model):
    def path_uploa(self, filename):
        return os.path.join(
            "articles",
            strftime("%Y/%m"),
            self.name.replace(" ", "_"),
            filename,
        )

    name = models.CharField(max_length=100, verbose_name="Article name.")
    description = models.TextField(verbose_name="Article text.")
    author = models.CharField(max_length=20, verbose_name="Author name.")
    image = models.ImageField(
        upload_to=path_uploa, verbose_name="Article image."
    )
    add_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Post time."
    )
    is_active = models.BooleanField(
        default=True, verbose_name="Active article."
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "articles"
        verbose_name = "Article for blog"
        verbose_name_plural = "Articles for blog"


class Comment(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    comment_author = models.CharField(
        max_length=20, verbose_name="Comment author name."
    )
    comment_text = models.CharField(
        max_length=255, verbose_name="Comment text."
    )
    add_time = models.DateTimeField(
        auto_now_add=True, verbose_name="Comment post time."
    )

    class Meta:
        db_table = "articles_comments"
        verbose_name = "Comment for article"
        verbose_name_plural = "Comments for article"

    def __str__(self):
        return self.comment_author

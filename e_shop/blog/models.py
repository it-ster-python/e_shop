import os
from django.core.exceptions import ValidationError
from django.db import models
from time import strftime
from django.utils import timezone
import datetime


class Article(models.Model):
    def path_upload(self, filename):
        return os.path.join(
                "article",
                strftime("%Y/%m"),
                self.title.replace(" ", "_"), filename)

    access_blogs = [
        ["access_admin", "access for admin"],
        ["access_user", "access for user"],
    ]
    title = models.CharField(max_length=100,
                             verbose_name=('Acticle title'),
                             help_text=("Article title"))
    date = models.DateField(default=timezone.now,
                            verbose_name=('Publication date'),
                            help_text=('Publication date'))
    # comment = models.CharField(max_length=250, verbose_name="Comment")
    access = models.CharField(
        max_length=50, choices=access_blogs, verbose_name="Access blogs ")
    image = models.ImageField(
        upload_to=path_upload, verbose_name="Blog image.")
    content = models.TextField()

    class Meta:
        db_table = "articles"
        verbose_name = "Article for blog"
        verbose_name_plural = "Articles for blog"

    def delete(self):
        try:
            os.remove(os.path.abspath(self.image))
        except Exception:
            pass

# 
# class Comments(models.Model):
#     comments_text = models.TextField()
#     comments_articles = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
#

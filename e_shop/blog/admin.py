from django.contrib import admin
from blog import models


class AdminArticle(admin.ModelAdmin):

    list_display = ["title"]


class AdminComment(admin.ModelAdmin):
    list_display = (
        "author",
        "comments_articles"
    )


admin.site.register(models.Article, AdminArticle),
admin.site.register(models.Comments, AdminComment)

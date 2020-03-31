from django.contrib import admin
from blog import models

class AdminArticle(admin.ModelAdmin):

    list_display = (
        "name",
        "add_time",
        "author",
        "is_active",
    )

class AdminComment(admin.ModelAdmin):

    list_display = (
        "comment_author",
        "comment_text",
        "add_time",
    )

admin.site.register(models.Article, AdminArticle)
admin.site.register(models.Comment, AdminComment)

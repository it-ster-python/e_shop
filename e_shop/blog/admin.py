from django.contrib import admin
from blog import models

class AdminArticle(admin.ModelAdmin):

    list_display = (
        "name",
        "add_time",
        "author",
        "is_active",
    )

admin.site.register(models.Article, AdminArticle)

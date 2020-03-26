from django.contrib import admin
from blog import models


class AdminArticle(admin.ModelAdmin):

    list_display = ["title"]


admin.site.register(models.Article, AdminArticle)

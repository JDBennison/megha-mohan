from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date_published', 'category')
    list_filter = ('category',)

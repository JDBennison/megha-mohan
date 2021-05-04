from django.shortcuts import render
from .models import Article


def articles(request):
    """A view to show all articles"""

    articles = Article.objects.order_by('date_published')

    context = {
        'articles': articles,
    }

    return render(request, 'articles/articles.html', context)

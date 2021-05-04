from django.shortcuts import render, HttpResponse


def articles(request):
    """A view to show all articles"""

    return render(request, 'articles/articles.html')

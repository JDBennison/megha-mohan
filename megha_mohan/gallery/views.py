from django.shortcuts import render
from .models import Image


def gallery(request):
    """A view to show all blog posts"""

    images = Image.objects.order_by('added_on')

    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)

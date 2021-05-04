from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from articles.models import Article


def index(request):
    """ A view to return the index page """
    articles = Article.objects.order_by('-date_published')[:3]
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            send_mail(subject, message, from_email, [
                'jamesbennison88@gmail.com', from_email])
    context = {
        'contact_form': contact_form,
        'articles': articles,
    }
    return render(request, 'home/index.html', context)

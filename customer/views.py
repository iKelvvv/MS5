from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import NewletterSubscribers
from .forms import ContactForm, NewsletterForm


# Create your views here.
def contact(request):
    """ A view to handle the customer contact form """

    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us. We will be in touch shortly.')
            return redirect(reverse('contact'))
            
    context = {
        'form': form
    }

    return render(request, 'customer/contact.html', context)


def newsletter(request):
    """ A view to handle the customer newsletter subscription """

    form = NewsletterForm()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewletterSubscribers.objects.filter(email=instance.email).exists():
                messages.error(request, 'You are already Subscribed')
            else:
                instance.save()
                messages.success(request, 'Thank you for subscribing to our newsletter!')
                return redirect(reverse('home'))

    context = {
        'form': form,
    }

    return render(request, 'customer/newsletter.html', context)

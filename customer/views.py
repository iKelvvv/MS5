from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact(request):
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
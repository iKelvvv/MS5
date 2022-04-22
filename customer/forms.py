from django import forms
from .models import CustomerContact, NewletterSubscribers


class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewletterSubscribers
        fields = ['email',]

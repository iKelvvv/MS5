from django import forms
from .models import CustomerContact


class ContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContact
        fields = '__all__'

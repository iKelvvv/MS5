from django.db import models


# Create your models here.
class CustomerContact(models.Model):
    """ A Model for the customer contact form """

    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(max_length=254, null=False, blank=False)


class NewletterSubscriber(models.Model):
    """ A Model for the customer newsletter subscription form """

    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

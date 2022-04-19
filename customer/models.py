from django.db import models


# Create your models here.
from django.db import models

# Create your models here.
class CustomerContact(models.Model):
    full_name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.CharField(max_length=254, null=False, blank=False)

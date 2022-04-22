from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('newsletter', views.newsletter, name='newsletter'),
]

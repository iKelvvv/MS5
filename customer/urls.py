from django.urls import path
from . import views

urlpatterns = [
    path('contact', views.contact, name='contact'),
    path('newsletter', views.newsletter, name='newsletter'),
    path(
        'newsletter/unsubscribe',
        views.newsletter_unsub,
        name='newsletter_unsub'),
    path('privacy-policy', views.privacy_policy, name='privacy_policy'),
]

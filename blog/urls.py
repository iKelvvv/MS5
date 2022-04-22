from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
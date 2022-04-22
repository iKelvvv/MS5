from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('add/', views.add_post, name='add_post'),
    path('edit/<slug:post>/', views.edit_post, name='edit_post'),
    path('delete/<slug:post>/', views.delete_post, name='delete_post'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]

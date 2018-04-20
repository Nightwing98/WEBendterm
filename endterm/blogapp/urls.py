from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blog/<int:blog_id>', views.blog_detail, name='blog_detail'),
    path('blog/<int:blog_id>/edit/', views.blog_edit, name="blog_edit"),
    path('blog/<int:blog_id>/delete/', views.blog_delete, name="blog_delete"),
    path('blog/new', views.blog_new, name="blog_new"),
]

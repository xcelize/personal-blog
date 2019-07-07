from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index.blog'),
    path('articles/<slug:slug_article>', views.article, name='view_article')
]
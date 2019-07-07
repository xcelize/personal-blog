from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout', views.log_out, name='logout')
]

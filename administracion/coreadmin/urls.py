from django.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from coreadmin import views

urlpatterns = [
    path('', views.home_view, name=''),
    path('home/', views.home_view, name='index.html'),
]
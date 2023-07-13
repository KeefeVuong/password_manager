from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('accounts/', views.accounts, name='accounts'),
    path('accounts/details/<int:id>', views.details, name='details'),
    path('', views.main, name='main'),
    path('register/', views.register, name='register'),
    path('', include("django.contrib.auth.urls")),
    path('create/', views.create, name='create')
]
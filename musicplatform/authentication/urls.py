from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register.as_view(),name="register"),
    path('login/', views.Login.as_view(),name="login"),
]
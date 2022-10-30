from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.get_artist_form,name="artist"),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.get_album_form,name="album"),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.get_artist_form.as_view(),name="artist"),
    path('', views.get_all_artist.as_view(),name="data"),
]
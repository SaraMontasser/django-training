from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('create/', login_required(views.get_artist_form.as_view()),name="artist"),
    path('', views.get_all_artist.as_view(),name="data"),
    path('data/', views.get_artist.as_view(),name="artistdata"),
]
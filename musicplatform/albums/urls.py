from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create/', views.get_album_form.as_view(),name="album"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
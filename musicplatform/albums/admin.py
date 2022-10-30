from django.contrib import admin
from albums.models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'release_datetime','cost','artist','is_approved')
    readonly_fields = ['created']

admin.site.register(Album,AlbumAdmin)
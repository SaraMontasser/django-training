from django.contrib import admin
from albums.models import Album

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'creation_datetime', 'release_datetime','cost','artist','isApproved')
    readonly_fields = ('creation_datetime')

admin.site.register(Album,AlbumAdmin)
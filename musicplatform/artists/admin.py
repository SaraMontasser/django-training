from django.contrib import admin
from artists.models import Artist

# Register your models here.

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Stage_name', 'Social_link', 'CountAlbums')
    
    def CountAlbums(self, artist):
        return artist.CountAlbums()
        
admin.site.register(Artist,ArtistAdmin)
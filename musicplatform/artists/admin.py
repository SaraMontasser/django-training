from django.contrib import admin
from artists.models import Artist
from albums.models import Album

# Register your models here.
class inlineAlbum(admin.StackedInline):
    model=Album
    extra=1

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Stage_name', 'Social_link', 'CountAlbums')
    inlines=[inlineAlbum]
    
    def CountAlbums(self, artist):
        return artist.CountAlbums()
        
admin.site.register(Artist,ArtistAdmin)
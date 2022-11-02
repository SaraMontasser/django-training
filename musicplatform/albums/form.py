from django import forms
from albums.models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model=Album
        fields=['name', 'release_datetime','cost','artist','is_approved']
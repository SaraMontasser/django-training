from django import forms
from albums.models import Album

class new_album(forms.ModelForm):
    class Meta:
        model=Album
        fields=['name', 'release_datetime','cost','artist','isApproved']
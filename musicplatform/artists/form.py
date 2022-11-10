from django import forms
from artists.models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model=Artist
        fields=['Stage_name', 'Social_link']
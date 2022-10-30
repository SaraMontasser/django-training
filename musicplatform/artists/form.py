from django import forms
from artists.models import Artist

class new_artist(forms.ModelForm):
    class Meta:
        model=Artist
        fields=['Stage_name', 'Social_link']
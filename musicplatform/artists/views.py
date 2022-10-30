from django.http import HttpResponseRedirect
from django.shortcuts import render
from artists.models import Artist
from .form import new_artist

def get_artist_form(request):
    if request.method == 'POST':
        form = new_artist(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = new_artist()
    return render(request, 'artist\\newArtist.html', {'form': form})

def get_all_artist(request):
    return render(request, 'artist\\displayArtists.html', {'Artist': Artist.objects.all()})
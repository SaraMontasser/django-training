from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import AlbumForm

def get_album_form(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, 'album\\newAlbum.html', {'form': form})
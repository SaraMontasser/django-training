from django.http import HttpResponseRedirect
from django.shortcuts import render

from .form import new_album

def get_album_form(request):
    if request.method == 'POST':
        form = new_album(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = new_album()
    return render(request, 'album\\newAlbum.html', {'form': form})
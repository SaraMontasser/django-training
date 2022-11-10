from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from artists.models import Artist
from .form import ArtistForm

class get_artist_form(View):
    form_class = ArtistForm
    template_name = 'artist\\newArtist.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})


class get_all_artist(View):
    query_set = Artist.objects.prefetch_related('album_set')
    template_name = 'artist\\displayArtists.html'

    def get(self, request):
        return render(request, self.template_name, {'query_set': self.query_set})
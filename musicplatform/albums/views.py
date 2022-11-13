from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .form import AlbumForm

class get_album_form(View):
    form_class = AlbumForm
    template_name = 'album\\newAlbum.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return render(request, self.template_name, {'form': form})

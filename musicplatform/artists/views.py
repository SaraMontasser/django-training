from django.http import HttpResponseRedirect,HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from artists.models import Artist
from .form import ArtistForm
from rest_framework.parsers import JSONParser
from artists.serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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

class get_artist(APIView):

    def get(self, request):
        Artists = Artist.objects.all()
        serializer = ArtistSerializer(Artists, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data("Stage_name","Social_link"),
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
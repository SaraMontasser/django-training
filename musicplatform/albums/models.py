from django.db import models
from artists.models import Artist

class Album(models.Model):
    name = models.CharField(max_length=200,default="New Album")
    creation_datetime = models.DateTimeField()
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=21, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
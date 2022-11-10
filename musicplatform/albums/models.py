from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

class Album(TimeStampedModel):
    name = models.CharField(max_length=200,default="New Album")
    release_datetime = models.DateTimeField(blank=False)
    cost = models.DecimalField(max_digits=21, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved=models.BooleanField(default=False,help_text='Approve the album if its name is not explicit')
    def __str__(self):
        return(" name: "+self.name+" creation date and time: "+self.creation_datetime.strftime("%m/%d/%Y, %H:%M:%S")+" release date and time: "+self.creation_datetime.strftime("%m/%d/%Y, %H:%M:%S")+" cost: "+str(self.cost))



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,default=album.name)
    image=models.ImageField(upload_to='media', blank=False)
    image_thumbnail=ImageSpecField(source='image', format='JPEG', processors=[ResizeToFill(100, 50)], options={'quality': 60})
    audio_file = models.FileField(upload_to="media",blank=False,validators=[FileExtensionValidator(['mp3', 'wav'])])


    def delete(self):
        if self.Song_set.all().count() > 1:
            super(Song, self).delete()
        else:
            raise ValidationError("Error, you can't delete all songs")
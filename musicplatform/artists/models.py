from django.db import models

class Artist(models.Model):

        
    Stage_name = models.CharField(max_length=20,unique=True,blank=False)
    Social_link = models.URLField(blank=True)
    

    def CountAlbums(self):
        return self.albums_set.filter(isApproved__exact=True).count()
    
    

    def __str__(self):
        return(" name: "+self.Stage_name+", Link: "+self.Social_link)


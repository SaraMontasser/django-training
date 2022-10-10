from enum import unique
from typing_extensions import Required
from django.db import models

class Artist(models.Model):
    Stage_name = models.CharField(max_length=20,unique=True,blank=False)
    Social_link = models.URLField(blank=True)

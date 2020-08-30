from django.db import models
from django.urls import reverse
# Create your models here.

class Plastic(models.Model): 
    name = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    artists = models.CharField(max_length=64)
    description = models.TextField(max_length=264)

    def __str__(self): 
        return self.name 
    
    def get_absolute_url(self): 
        return reverse("Plastic")
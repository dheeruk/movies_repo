from django.db import models

# Create your models here.
class AddMoviesModel(models.Model):
    movieName=models.CharField(max_length=100)
    actorName=models.CharField(max_length=100)
    actressName=models.CharField(max_length=100)
    releaseDate=models.DateField()
    rating=models.IntegerField()

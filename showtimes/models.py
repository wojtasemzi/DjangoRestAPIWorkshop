from django.db import models

from movies import models as movie_models


class Cinema(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    movies = models.ManyToManyField(movie_models.Movie, through='Screening')


class Screening(models.Model):
    movie = models.ForeignKey(movie_models.Movie, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    date = models.DateTimeField()

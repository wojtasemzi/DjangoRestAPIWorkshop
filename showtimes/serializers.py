from pyrsistent import field
from rest_framework import serializers
from movies import models as models_movies
from showtimes import models as models_showtimes


class Cinema(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True,
                                                 read_only=True,
                                                 view_name='movie')

    class Meta:
        model = models_showtimes.Cinema
        fields = ('id', 'name', 'city', 'movies')


class Screening(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(slug_field='name',
                                           queryset=models_showtimes.Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title',
                                          queryset=models_movies.Movie.objects.all())

    class Meta:
        model = models_showtimes.Screening
        fields = ('movie', 'cinema', 'date')

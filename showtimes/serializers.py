from rest_framework import serializers
from showtimes import models as models_showtimes


class Cinema(serializers.ModelSerializer):
    movies = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie')

    class Meta:
        model = models_showtimes.Cinema
        fields = ('id', 'name', 'city', 'movies')

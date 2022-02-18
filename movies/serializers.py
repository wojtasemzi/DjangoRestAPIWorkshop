from rest_framework import serializers
from movies import models


class Movie(serializers.ModelSerializer):
    actors = serializers.SlugRelatedField(many=True, slug_field='name', queryset=models.Person.objects.all())
    director = serializers.SlugRelatedField(slug_field='name', queryset=models.Person.objects.all())

    class Meta:
        model = models.Movie
        fields = ("id", "title", "year", "description", "director", "actors")

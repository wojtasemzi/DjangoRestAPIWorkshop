from movies import models
from movies import serializers
from rest_framework import generics


class Movies(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.Movie


class Movie(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.Movie
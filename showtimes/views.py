from showtimes import models
from showtimes import serializers
from rest_framework import generics


class Cinemas(generics.ListCreateAPIView):
    queryset = models.Cinema.objects.all()
    serializer_class = serializers.Cinema

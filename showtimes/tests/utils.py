from random import sample

from movies import models as models_movies


def random_movies(numer_of_movies=3):
    """ Return 3 (by default) random Movie objects. """
    movies = list(models_movies.Movie.objects.all())
    return sample(movies, numer_of_movies)
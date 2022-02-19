from random import sample
from faker import Faker

from movies import models as models_movies
from showtimes import models as models_showtimes

faker = Faker('pl_PL')


def random_movies(numer_of_movies=3):
    """ Return 3 (by default) random Movie objects. """
    movies = list(models_movies.Movie.objects.all())
    return sample(movies, numer_of_movies)


def add_screening(cinema, number_of_movies=3):
    """ Adds 3 (by default) screenings for provided cinema. """
    movies = random_movies(number_of_movies)
    for movie in movies:
        models_showtimes.Screening.objects.create(
                cinema=cinema,
                movie=movie,
                date=faker.date_time_between())


def fake_cinema():
    """ Generate fake cinema data """
    return {'name': faker.name(),
            'city': faker.city()}


def add_cinema():
    """ Add cinema """
    cinema = models_showtimes.Cinema.objects.create(**fake_cinema())
    add_screening(cinema)

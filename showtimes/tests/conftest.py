import pytest
from faker import Faker
from rest_framework.test import APIClient

from movies import models as models_movies
from movies.tests.utils import create_fake_movie
from showtimes.tests.utils import add_cinema

faker = Faker('pl_PL')


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        models_movies.Person.objects.create(name=faker.name())
    for _ in range (10):
        create_fake_movie()
    for _ in range(3):
        add_cinema()

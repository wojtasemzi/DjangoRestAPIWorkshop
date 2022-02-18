import os
import sys

import pytest
from rest_framework.test import APIClient

from .. import models
from .utils import faker, create_fake_movie

sys.path.append(os.path.dirname(__file__))


@pytest.fixture
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    for _ in range(5):
        models.Person.objects.create(name=faker.name())
    for _ in range(3):
        create_fake_movie()

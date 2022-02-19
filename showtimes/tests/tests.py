from django.urls import reverse
import pytest

from showtimes import models as models_showtimes
from .utils import fake_cinema


@pytest.mark.django_db
def test_cinema_add(client, set_up):
    cinemas_before = models_showtimes.Cinema.objects.count()
    new_cinema = fake_cinema()
    response = client.post(reverse('cinemas'), new_cinema, format='json')
    assert response.status_code == 201
    assert models_showtimes.Cinema.objects.count() == cinemas_before + 1
    for key, value in new_cinema.items():
        assert key in response.data
        if isinstance(value, list):
            assert len(response.data[key]) == len(value)
        else:
            assert response.data[key] == value
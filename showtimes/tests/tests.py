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


@pytest.mark.django_db
def test_cinema_get_list(client, set_up):
    response = client.get(reverse('cinemas'), {}, format='json')
    assert response.status_code == 200
    assert models_showtimes.Cinema.objects.count() == len(response.data)


@pytest.mark.django_db
def test_cinema_get_detail(client, set_up):
    cinema = models.Cinema.objects.first()
    response = client.get(f'/cinemas/{cinema.id}', {}, format='json')
    #TODO:                reverse('cinema', {'id': cinema.id})
    assert response.status_code == 200
    for field in ('name', 'city', 'movies'):
        assert field in response.data


@pytest.mark.django_db
def test_cinema_update(client, set_up):
    cinema = models_showtimes.Cinema.objects.first()
    response = client.get(f'/cinemas/{cinema.id}', {}, format='json')
    #TODO:                reverse('cinema', {'id': cinema.id})
    cinema_data = response.data
    new_name = 'new_name'
    new_city = 'new_city'
    cinema_data['name'] = new_name
    cinema_data['city'] = new_city
    response = client.patch(f'/cinemas/{cinema.id}', cinema_data, format='json')
    #TODO:                reverse('cinema', {'id': cinema.id})
    assert response.status_code == 200
    cinema_updated = models_showtimes.Cinema.objects.get(id=cinema.id)
    assert cinema_updated.name == new_name
    assert cinema_updated.city == new_city


@pytest.mark.django_db
def test_cinema_delete(client, set_up):
    cinema = models_showtimes.Cinema.objects.first()
    response = client.delete(f'/cinemas/{cinema.id}', {}, format='json')
    #TODO:                reverse('cinema', {'id': cinema.id})
    assert response.status_code == 204
    cinemas_id = [cinema.id for cinema in models_showtimes.Cinema.objects.all()]
    assert cinema.id not in cinemas_id

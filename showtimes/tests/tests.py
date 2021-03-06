from django.urls import reverse
import pytest

from movies import models as models_movies
from showtimes import models as models_showtimes
from .utils import fake_cinema, fake_screening_data

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
    cinema = models_showtimes.Cinema.objects.first()
    response = client.get(reverse('cinema', args=(cinema.id,)), {}, format='json')
    assert response.status_code == 200
    for field in ('name', 'city', 'movies'):
        assert field in response.data


@pytest.mark.django_db
def test_cinema_update(client, set_up):
    cinema = models_showtimes.Cinema.objects.first()
    response = client.get(reverse('cinema', args=(cinema.id,)), {}, format='json')
    cinema_data = response.data
    new_name = 'new_name'
    new_city = 'new_city'
    cinema_data['name'] = new_name
    cinema_data['city'] = new_city
    response = client.patch(reverse('cinema', args=(cinema.id,)),
                            cinema_data,
                            format='json')
    assert response.status_code == 200
    cinema_updated = models_showtimes.Cinema.objects.get(id=cinema.id)
    assert cinema_updated.name == new_name
    assert cinema_updated.city == new_city


@pytest.mark.django_db
def test_cinema_delete(client, set_up):
    cinema = models_showtimes.Cinema.objects.first()
    response = client.delete(reverse('cinema', args=(cinema.id,)), {}, format='json')
    assert response.status_code == 204
    cinemas_id = [cinema.id for cinema in models_showtimes.Cinema.objects.all()]
    assert cinema.id not in cinemas_id


@pytest.mark.django_db
def test_screening_add(client, set_up):
    screenings_before = models_showtimes.Screening.objects.count()
    new_screening = fake_screening_data()
    response = client.post(reverse('screenings'), new_screening, format='json')
    assert response.status_code == 201
    assert models_showtimes.Screening.objects.count() == screenings_before + 1
    for key, value in new_screening.items():
        assert key in response.data
        if isinstance(value, list):
            assert len(response.data[key]) == len(value)
        else:
            assert response.data[key] == value


@pytest.mark.django_db
def test_screening_get_list(client, set_up):
    response = client.get(reverse('screenings'), {}, format='json')
    assert response.status_code == 200
    assert models_showtimes.Screening.objects.count() == len(response.data)


@pytest.mark.django_db
def test_screening_get_detail(client, set_up):
    screening = models_showtimes.Screening.objects.first()
    response = client.get(reverse('screening', args=(screening.id,)), {}, format='json')
    assert response.status_code == 200
    for field in ('movie', 'cinema', 'date'):
        assert field in response.data


@pytest.mark.django_db
def test_screening_update(client, set_up):
    screening = models_showtimes.Screening.objects.first()
    response = client.get(reverse('screening', args=(screening.id,)), {}, format='json')
    screening_data = response.data
    new_movie = models_movies.Movie.objects.last()
    new_cinema = models_showtimes.Cinema.objects.last()
    new_date = '2021-05-29T18:46:56Z'
    screening_data['movie'] = new_movie.title
    screening_data['cinema'] = new_cinema.name
    screening_data['date'] = new_date
    response = client.patch(reverse('screening', args=(screening.id,)),
                            screening_data,
                            format='json')
    assert response.status_code == 200
    screening_updated = models_showtimes.Screening.objects.get(id=screening.id)
    assert screening_updated.movie == new_movie
    assert screening_updated.cinema == new_cinema
    assert screening_updated.date == new_date

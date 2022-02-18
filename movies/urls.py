from django.urls import path
from movies import views

# all paths start with movies/
urlpatterns = [
    path('', views.Movies.as_view(), name='movies'),
    path('<int:pk>/', views.Movie.as_view(), name='movie'),
]

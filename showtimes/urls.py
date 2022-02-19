from django.urls import path
from showtimes import views

# all paths start with cinemas/
urlpatterns = [
    path('', views.Cinemas.as_view(), name='cinemas'),
    path('<int:pk>/', views.Cinema.as_view(), name='cinema'),
    path('screenings/', views.Screenings.as_view(), name='screenings'),
    path('screenings/<int:pk>/', views.Screaning.as_view(), name='screening'),
]

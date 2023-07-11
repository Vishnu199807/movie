from django.urls import path
from .views import MovieListCreateView


urlpatterns = [
    path('movie/', MovieListCreateView.as_view(), name='movie-create'),
]
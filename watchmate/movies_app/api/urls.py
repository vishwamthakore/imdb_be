from django.urls import path
from movies_app.api import views

urlpatterns = [
    path("movies", views.MovieListAV.as_view(), name="movies"),
    path("movies/<int:id>", views.MovieDetailAV.as_view() , name="movie-detail"),
    path("platforms", views.PlatformListAV.as_view(), name="platforms"),
    path("movies/<int:id>/reviews", views.ReviewListAV.as_view() , name="reviews")
    
]

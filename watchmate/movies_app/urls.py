from django.urls import path
from movies_app import views

urlpatterns = [
    path("movies", views.MovieListView.as_view(), name="movie-list"),
    path("movies/<int:id>", views.MovieDetailView.as_view() , name="movie-detail"),
    path("platforms", views.PlatformListView.as_view(), name="platforms"),
    path("movies/<int:id>/reviews", views.ReviewListView.as_view() , name="reviews")
    
]

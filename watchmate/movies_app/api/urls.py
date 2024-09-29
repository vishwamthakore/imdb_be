from django.urls import path
from movies_app.api import views

urlpatterns = [
    path("", views.MovieListAV.as_view(), name="movies"),
    path("<int:id>", views.MovieDetailAV.as_view() , name="movie-detail")
]

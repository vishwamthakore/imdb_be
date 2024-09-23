from django.urls import path
from movies_app.api import views

urlpatterns = [
    path("", views.get_all_movies, name="movies"),
    path("<int:id>", views.get_movie, name="movie-detail")
]

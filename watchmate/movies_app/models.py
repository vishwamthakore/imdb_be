from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Platform(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)
    average_rating = models.FloatField(default=0)
    total_ratings = models.IntegerField(default=0)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name="movie_set")
    
    def __str__(self):
        return self.name
    
    
class Review(models.Model):
    RATINGS = [
        (1 , "1 - Bad"),
        (2 , "2 - Average"),
        (3 , "3 - Good"),
        (4 , "4 - V Good"),
        (5 , "5 - Excellent")
    ]
    
    rating = models.IntegerField(choices=RATINGS)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.rating} | {self.movie.name}"
    
    

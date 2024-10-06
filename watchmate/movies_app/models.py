from django.db import models
from django.utils import timezone


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
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, related_name="movie_set")
    
    def __str__(self):
        return self.name
    

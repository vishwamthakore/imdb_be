from django.contrib import admin

from .models import Movie, Platform, Review

admin.site.register(Movie)
admin.site.register(Platform)
admin.site.register(Review)

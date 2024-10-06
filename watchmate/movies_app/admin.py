from django.contrib import admin

from .models import Movie, Platform

admin.site.register(Movie)
admin.site.register(Platform)
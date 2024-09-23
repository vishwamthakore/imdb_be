from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movies_app.models import Movie



def get_all_movies(request):
    movies = Movie.objects.all()
    movies_dict = {"data" : list(movies.values())}
    
    return JsonResponse(movies_dict)
    # return HttpResponse("Hello World")
    
def get_movie(request, id):
    movie = Movie.objects.get(id=id)
    
    movie_dict = {
        "id" : movie.id,
        "name" : movie.name,
        "description" : movie.description
    }
    print(movie_dict)
    
    return JsonResponse(movie_dict)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movies_app.models import Movie
from movies_app.serializers import  MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def get_all_movies(request):
    
    if request.method == 'GET':
        movies = Movie.objects.all()    
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    
    elif request.method == 'POST':
        print(request.data, type(request.data))
        serializer = MovieSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=400)
        


@api_view(['GET', 'PUT', 'DELETE'])  
def get_movie(request, id):
    
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        movie = Movie.objects.get(id=id)
        serializer = MovieSerializer(movie, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        movie = Movie.objects.get(id=id)
        movie.delete()
        return HttpResponse(status=204)

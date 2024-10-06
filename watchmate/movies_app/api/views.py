from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movies_app.models import Movie, Platform
from movies_app.serializers import  MovieSerializer, PlatformSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class PlatformListAV(APIView):
    def get(self, request):
        platforms = Platform.objects.all()
        serializer = PlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PlatformSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        

class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()    
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
        

class MovieDetailAV(APIView):
    
    def get_object(self, id):
        try:
            movie = Movie.objects.get(id=id)
            return movie
        except Movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
        
    def put(self, request, id):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
    def delete(self, request, id):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# @api_view(['GET', 'POST'])
# def get_all_movies(request):
    
#     if request.method == 'GET':
#         movies = Movie.objects.all()    
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

    
#     elif request.method == 'POST':
#         print(request.data, type(request.data))
#         serializer = MovieSerializer(data = request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
        


# @api_view(['GET', 'PUT', 'DELETE'])  
# def get_movie(request, id):
    
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         movie = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         movie = Movie.objects.get(id=id)
#         serializer = MovieSerializer(movie, data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return JsonResponse(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(id=id)
#         movie.delete()
#         return HttpResponse(status=204)

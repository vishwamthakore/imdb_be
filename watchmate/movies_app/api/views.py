from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from movies_app.models import Platform, Movie, Review
from movies_app.serializers import  MovieSerializer, PlatformSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated


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
    permission_classes = [IsAuthenticated]
    
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
    
    

class ReviewListAV(APIView):
    
    def checkMovieExists(self, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            return True
        except Movie.DoesNotExist:
            print("movie does not exist")
            return False
        
    
    def get(self, request, id):
        # get the reviews of this id movie fram the table
        # return in form of dict
        if not self.checkMovieExists(movie_id = id):
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        movie_reviews = Review.objects.filter(movie_id=id)
        serializer = ReviewSerializer(movie_reviews, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, id):
        self.checkMovieExists(movie_id = id)
        
        print("review data", request.data)
        request.data["movie"] = id
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        

from django.shortcuts import get_object_or_404
from django.db.models import Avg
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import  (DirectorSerializer, MovieSerializer, ReviewSerializer,
                DirectorValidaterSerializer, MovieValidaterSerializer, RiviewValidaterSerializer)


@api_view(['GET', 'POST'])
def director_list(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DirectorValidaterSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            Director.objects.create(name= serializer.validated_data['name'])
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE', 'PUT'])
def director_detail(request, id):
    director = get_object_or_404(Director, id=id)

    if request.method == 'GET':
        serializer = DirectorSerializer(director)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = DirectorValidaterSerializer(data=request.data)
        if serializer.is_valid():
            director.name = serializer.validated_data['name']
            director.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieValidaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Movie.objects.create(
                title=serializer.validated_data['title'],
                description =serializer.validated_data['description'],
                duration=serializer.validated_data['duration']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MovieValidaterSerializer(data=request.data)
        if serializer.is_valid():
            movie.title = serializer.validated_data['title']
            movie.description = serializer.validated_data['description']
            movie.duration = serializer.validated_data['duration']
            movie.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RiviewValidaterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Review.objects.create(
                text=serializer.validated_data['text'],
                stars=serializer.validated_data['stars']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RiviewValidaterSerializer(data=request.data)
        if serializer.is_valid():
            review.text = serializer.validated_data['text']
            review.stars = serializer.validated_data['stars']
            review.save()
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

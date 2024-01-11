from rest_framework import serializers
from .models import Director, Movie, Review



class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id', 'name']


class DirectorValidaterSerializer(serializers.Serializer):
    name = serializers.CharField()



class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director']


class MovieValidaterSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    duration = serializers.IntegerField()



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['id', 'text', 'stars', 'movie']


class RiviewValidaterSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()

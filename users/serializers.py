from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from .models import UserConfirmation




class UserValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()


class AuthorizeValidateSerializer(UserValidateSerializer):
    def validate_password(self, password):
        return password



class RegisterValidateSerializer(UserValidateSerializer):
    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('User already exists!')


class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirmation
        fields = ['code']

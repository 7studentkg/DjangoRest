from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .randomcode import generate_random_code
from .serializers import RegisterValidateSerializer, AuthorizeValidateSerializer, UserConfirmationSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import UserConfirmation
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from django.shortcuts import get_object_or_404




@api_view(['POST'])
def register_api_view(request):

    serializer = RegisterValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = request.data.get('username')
    password = request.data.get('password')

    User.objects.create_user(username=username, password=password, is_active=False)
    confirmation = UserConfirmation.objects.create(username=username, code=generate_random_code())
    return Response({'status': 'User successfully registered!', 'code': confirmation.code},
                    status=HTTP_201_CREATED)

@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')
    confirmation = get_object_or_404(UserConfirmation, code=code)
    user = confirmation.user
    user.is_active = True
    user.save()
    confirmation.delete()
    return Response({'status': 'User activated'}, status=HTTP_200_OK)


@api_view(['POST'])
def authorize_api_view(request):

    serializer = AuthorizeValidateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(**serializer.validated_data)

    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'key': token.key})
    return Response(status=403, data={'error': 'User credential error!'})


@api_view(['GET'])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message': 'User logged out'}, status=HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({'message': 'User is already logged out'}, status=HTTP_200_OK)

from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_api_view),
    path('users/confirm/', views.confirm_user_api_view),
    path('authorize/', views.authorize_api_view),
    path('users/logout/', views.logout),
]

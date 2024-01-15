from django.urls import path

from . import views

urlpatterns = [
    # path('directors/', views.director_list),
    path('directors/', views.DirectorsListAPIView.as_view()),
    # path('directors/<int:id>/', views.director_detail),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    # path('movies/', views.movie_list),
    path('movies/', views.MovieListCreateAPIView.as_view()),
    # path('movies/<int:id>/', views.movie_detail),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    # path('reviews/', views.review_list),
    path('reviews/', views.ReviewListCreateAPIView.as_view()),
    # path('reviews/<int:id>/', views.review_detail),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]

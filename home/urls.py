from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet, name='tweet'),
    path('iuadsfkjadslfalksdgfasdflasidugafkjdfasd/like/', views.like_tweet, name='likeTweet'),
    path('<str:username>/status/<str:tweetid>/', views.status, name='status'),
]
from django.urls import path, include

from .views import home_view, tweet_detail_view

app_name = 'tweets_app'

urlpatterns = [
    path('', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view),
]

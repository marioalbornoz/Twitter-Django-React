from django.urls import path, include

from .views import home_view, tweet_detail_view, tweet_list_view, Create_tweet

app_name = 'tweets_app'

urlpatterns = [
    path('', home_view, name='home'),
    path('tweets/', tweet_list_view, name="tweet_list"),
    path('tweets/<int:tweet_id>', tweet_detail_view),
    path("tweets/create-tweet/", Create_tweet.as_view(), name="tweet_crear"),
]

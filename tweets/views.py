from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Create your views here.

def home_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hola Mundo </h1>")

def tweet_detail_view(request,tweet_id, *args, **kwargs):

    data = {
        'tweet_id':tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not found'
        status = 404
    
    return JsonResponse(data, status = status)
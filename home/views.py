from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tweet
from django.contrib.auth.decorators import login_required


def home(request):
    tweets = Tweet.objects.all()
    context = {'title': '', 'tweets': tweets}
    if request.user.is_authenticated:
        context['title'] = 'Home'
        return render(request, 'home/home/home.html', context)
    else:
        context['title'] = 'Explore'
        return render(request, 'home/home/home.html', context)


@login_required(login_url='login')
def tweet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet = Tweet.objects.create(
            user=request.user, content=request.POST.get('content'))
        tweet.save()
        return redirect('home')
    context = {'title': 'Tweet'}
    return render(request, 'home/tweet.html', context)


def like_tweet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet_id = request.POST.get('id')
        tweet = Tweet.objects.get(id=tweet_id)
        if request.user in tweet.like.all():
            tweet.like.remove(request.user)
        else:
            tweet.like.add(request.user)
        tweet.save()
    return redirect('home')


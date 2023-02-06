from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tweet


def home(request):
    context = {'title': ''}
    if request.user.is_authenticated:
        context['title'] = 'Home'
        return render(request, 'home/home/home.html', context)
    else:
        context['title'] = 'Explore'
        return render(request, 'home/home/home.html', context)


def tweet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet = Tweet.objects.create(
            user=request.user, content=request.POST.get('content'))
        tweet.save()
        return redirect('home')
    return redirect('home')

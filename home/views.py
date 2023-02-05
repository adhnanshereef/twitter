from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    context = {'title': ''}
    if request.user.is_authenticated:
        context['title']='Home'
    else:
        context['title']='Explore'
    return render(request, 'home/home.html', context)

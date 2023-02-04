from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    context = {'title': 'Explore'}
    return render(request, 'home/home.html', context)

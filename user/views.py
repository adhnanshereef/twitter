from django.shortcuts import render, redirect
from django.http import HttpResponse


def signup(request):
    context = {'title': 'Sign up for Twitter'}
    return render(request, 'user/signup.html', context)

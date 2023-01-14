from django.shortcuts import render, redirect
from django.http import HttpResponse

def signup(request):
    return HttpResponse(request.user.email)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import User


def signup(request):
    context = {'title': 'Sign up for Twitter'}
    return render(request, 'user/signup/signup.html', context)


def signupwithemail(request):
    context = {'title': 'Sign up for Twitter'}
    if request.method == "POST":
        if request.session['step'] == 1:
            request.session['temp']['name'] = request.POST.get('name')
            request.session['temp']['email'] = request.POST.get('email')
            request.session['temp']['date'] = f"{request.POST.get('month')} {request.POST.get('day')}, {request.POST.get('year')}"
            request.session['step'] = 2
            request.session.save()
            context['step'] = request.session['step']
            return render(request, 'user/signup/email-signup.html', context)
        elif request.session['step'] == 2:
            request.session['temp']['track-web'] = request.POST.get(
                'track-web')
            request.session['step'] = 3
            request.session.save()
            context['step'] = request.session['step']
            context['data'] = request.session['temp']
            return render(request, 'user/signup/email-signup.html', context)
        elif request.session['step'] == 3 or request.session['step'] == 4:
            if request.session['step'] == 3:
                request.session['step'] = 4
            else:
                request.session['step'] = 5
            request.session.save()
            context['step'] = request.session['step']
            context['data'] = request.session['temp']
            return render(request, 'user/signup/email-signup.html', context)
        elif request.session['step'] == 5:
            data = request.session['temp']
            password = make_password(request.POST.get('password'))
            username = request.POST.get('username')
            if User.objects.filter(email=data['email']).exists():
                request.session['step'] = 3
                request.session.save()
                messages.error(
                    request, 'Email already exist! Please use another one')
                return render(request, 'user/signup/step3.html')
            else:
                user = User.objects.create(name=data['name'], email=data['email'], username=username,
                                           dateofbirth=data['date'], password=password)
                request.session.clear()
                login(request, user)
                return redirect('home')

    if request.method == 'GET':
        request.session['temp'] = {}
        request.session['step'] = 1
    context['step'] = request.session['step']
    context['data'] = request.session['temp']
    return render(request, 'user/signup/email-signup.html', context)


def signout(request):
    if not request.user.is_authenticated:
        return redirect('home')
    logout(request)
    return redirect('home')


def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Account Doesn't exist")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_post=request.POST.get('next_url')
            if next_post:
                return redirect(next_post)
            else:
                return redirect('home')
            
        else:
            messages.error(request, 'Password went wrong')
    next_url = request.GET.get('next')
    context = {'title': 'Login in to Twitter','next':next_url}
    return render(request, 'user/login/login.html', context)

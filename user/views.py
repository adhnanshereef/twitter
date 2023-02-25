from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from urllib.parse import urlparse
from .models import User


def signup(request):
    context = {'title': 'Sign up for Twitter'}
    return render(request, 'user/signup/signup.html', context)


def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


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
            next_post = request.POST.get('next_url')
            if next_post:
                return redirect(next_post)
            else:
                return redirect('home')

        else:
            messages.error(request, 'Password went wrong')
    next_url = request.GET.get('next')
    context = {'title': 'Login in to Twitter', 'next': next_url}
    return render(request, 'user/login/login.html', context)


def follow(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        who = request.user
        whom = User.objects.get(username=request.POST.get('whom'))
        if who == whom:
            return redirect('home')
        if who in whom.followers.all() and whom in who.following.all():
            whom.followers.remove(who)
            who.following.remove(whom)
        else:
            whom.followers.add(who)
            who.following.add(whom)
        who.save()
        whom.save()
        who.refresh_from_db()
        print(User.objects.get(username=who.username).following.all())
        print(whom.followers.all())
        if 'current_url' in request.POST:
            return redirect(request.POST['current_url'])

    return redirect('home')


def edit(request):
    user = request.user
    if request.method == 'POST':
        name = request.POST['name']
        bio = request.POST['bio']
        website = request.POST['website']
        location = request.POST['location']
        if len(name) < 51:
            user.name = name
        else:
            messages.error(request, "Name must be under 50 letters")

        if len(bio) < 161:
            user.bio = bio
        else:
            messages.error(request, "Bio must be under 160 letters")

        if len(location) < 30:
            user.location = location
        else:
            messages.error(request, "Bio must be under 30 letters")

        if is_valid_url(website):
            user.website = website
        else:
            messages.error(request, "Enter valid url")
        user.save()
        user.refresh_from_db()
        return redirect('profile', username=user.username)
    context = {'title': f'{user.name} (@{user.username})', 'user': user}
    return render(request, 'user/profile/edit.html', context)

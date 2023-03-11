from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tweet, TweetMedia
from user.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    tweets = Tweet.objects.all()
    domain = request.get_host()
    context = {'title': '', 'tweets': tweets, "domain": domain}
    if request.user.is_authenticated:
        context['title'] = 'Home'
        return render(request, 'home/home/home.html', context)
    else:
        context['title'] = 'Explore'
        return render(request, 'home/home/home.html', context)


# Profile
def profile(request, username):
    context = {'title': ''}
    try:
        user = User.objects.get(username=username)
    except:
        context['title'] = 'Profile'
        return HttpResponse('This account doesn’t exist')
    if user != None:
        tweets = user.tweet_set.all()
        context = {
            'title': f"{user.name} (@{user.username})", 'user': user, 'tweets': tweets}
        return render(request, 'home/profile/profile.html', context)
    else:
        context['title'] = 'Profile'
        return HttpResponse('This account doesn’t exist')


def followers(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        context['title'] = 'Profile'
        return HttpResponse('This account doesn’t exist')
    if user != None:
        followers = user.followers.all()
        context = {
            'title': f'People following {user.name} (@{user})', 'follows': followers, 'user': user}
        return render(request, 'home/profile/followers.html', context)
    else:
        return HttpResponse('This account doesn’t exist')


def following(request, username):
    try:
        user = User.objects.get(username=username)
    except:
        context['title'] = 'Profile'
        return HttpResponse('This account doesn’t exist')
    if user != None:
        following = user.following.all()
        context = {
            'title': f'People followed by {user.name} (@{user})', 'follows': following, 'user': user}
        return render(request, 'home/profile/following.html', context)
    else:
        return HttpResponse('This account doesn’t exist')


# Tweet views start

@login_required(login_url='login')
def tweet(request):
    if request.method == 'POST' and request.user.is_authenticated:
        tweet = Tweet.objects.create(
            user=request.user, content=request.POST.get('content'))
        medias = request.FILES.getlist('medias')
        if medias:
            for media in medias:
                media_ext = media.name.split('.')[-1]
                if media_ext in ['jpg', 'jpeg', 'png', 'gif', 'mp4', 'webm']:
                    tweet_media = TweetMedia.objects.create(
                        media=media,ext=media_ext)
                    tweet.medias.add(tweet_media)
                else:
                    messages.error(
                    request, 'Unsupported file')
                    tweet.delete()
                    return redirect('tweet')
        tweet.save()
        return redirect('home')
    context = {'title': 'Tweet'}
    return render(request, 'home/tweet/tweet.html', context)


def status(request, username, tweetid):
    try:
        user_checkup = User.objects.get(username=username)
        tweet = Tweet.objects.get(id=tweetid)
        user = tweet.user
    except:
        user_checkup = None
        tweet = None
        user = None
    if user == None or tweet == None or user_checkup == None:
        return HttpResponse('Hmm...this page doesn’t exist. Try searching for something else.')
    if user_checkup != user:
        return HttpResponse('Hmm...this page doesn’t exist. Try searching for something else.')
    context = {
        'title': f'{user.name} on Twitter: "{tweet.content[:20]}" / Twitter', 'tweet': tweet, 'user': user}
    return render(request, 'home/tweet/status.html', context)


def like_tweet(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        tweet_id = request.POST.get('id')
        tweet = Tweet.objects.get(id=tweet_id)
        if request.user in tweet.like.all():
            tweet.like.remove(request.user)
        else:
            tweet.like.add(request.user)
        tweet.save()
        where = request.POST.get('where')
        if where:
            return redirect(where)
    return redirect('home')

# Tweet views end

from django.db import models
from user.models import User

# Image of Tweet
class TweetImage(models.Model):
    image = models.ImageField(upload_to='tweets/')

# reply for Tweet
class TweetReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, max_length=200)
    like = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

# Views of Tweet
class TweetViews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    impression = models.IntegerField(default=0)
    engagements = models.IntegerField(default=0)
    detail_expands = models.IntegerField(default=0)
    new_follower = models.IntegerField(default=0)
    profile_visits = models.IntegerField(default=0)

# Main Tweet Model
class Tweet(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    content = models.TextField(null=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(
        TweetImage, related_name='images', blank=True)
    like = models.ManyToManyField(
        User, related_name='like', blank=True)
    reply = models.ManyToManyField(
        TweetReply, related_name='comments', blank=True)
    retweet = models.ManyToManyField(
        User, related_name='retweet', blank=True)
    views = models.ManyToManyField(
        TweetViews, related_name='views', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:50]

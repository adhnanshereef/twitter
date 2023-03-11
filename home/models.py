from django.db import models
from user.models import User
import os
import uuid

# To get random name for Medias in Tweet
def tweetmedia_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('tweets/', filename)
    

# Media in Tweet
class TweetMedia(models.Model):
    media = models.FileField(upload_to=tweetmedia_filename)
    ext = models.CharField(null=True, blank=True, max_length=100)
    def delete(self, *args, **kwargs):
        self.media.delete()
        super().delete(*args, **kwargs)


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
    medias = models.ManyToManyField(
        TweetMedia, related_name='medias', blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.ManyToManyField(User, related_name='like', blank=True)
    reply = models.ManyToManyField(
        TweetReply, related_name='reply', blank=True)
    retweet = models.ManyToManyField(User, related_name='retweet', blank=True)
    views = models.ManyToManyField(
        TweetViews, related_name='views', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:50]

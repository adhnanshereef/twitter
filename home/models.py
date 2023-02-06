from django.db import models
from user.models import User


# Tweet Related Models
class TweetImage(models.Model):
    image = models.ImageField(upload_to='tweets/', null=True)


class TweetReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, max_length=200)
    like = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

# Main Tweet Model
class Tweet(models.Model):
    content = models.TextField(null=True, max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ManyToManyField(
        TweetImage, related_name='images', blank=True)
    like = models.IntegerField(default=0)
    reply = models.ManyToManyField(
        TweetReply, related_name='comments', blank=True)
    reply_count = models.IntegerField(default=0)
    retweet = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.content[:50]

# Tweet Related Models End

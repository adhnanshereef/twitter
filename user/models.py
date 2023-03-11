from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.core.validators import URLValidator
import os
import uuid
from django.conf import settings


# To get random name for avatar
def avatar_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return os.path.join('avatar/', filename)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, blank=False, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, max_length=160)
    website = models.URLField(validators=[URLValidator()], blank=True)
    location = models.CharField(max_length=30, blank=True)
    following = models.ManyToManyField(
        'self', related_name='folowing', blank=True, symmetrical=False)
    followers = models.ManyToManyField(
        'self', related_name='folower', blank=True, symmetrical=False)
    dateofbirth = models.DateField(blank=True, null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(
        upload_to=avatar_filename, null=True, blank=True, default="avatar/avatar.svg")
    banner = models.ImageField(
        upload_to='banner/', null=True, blank=True, default="banner/banner.jpg")
    theme = models.CharField(max_length=10, blank=True, default='light')
    is_staff = models.BooleanField(blank=True, null=True)
    is_superuser = models.BooleanField(blank=True, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email',]
    objects = UserManager()

    def __str__(self):
        return self.username

    def delete(self, *args, **kwargs):
        if self.avatar.url != settings.MEDIA_URL + 'avatar/avatar.svg':
            self.avatar.delete()
        super().delete(*args, **kwargs)

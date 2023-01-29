from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# User Model


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, blank=False, unique=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    dateofbirth = models.CharField(max_length=100,blank=True,null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, default="avatar/avatar.svg")
    theme = models.CharField(max_length=10, blank=True, default='light')
    is_staff = models.BooleanField(blank=True,null=True)
    is_superuser = models.BooleanField(blank=True,null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email',]
    objects = UserManager()

    def __str__(self):
        return self.username

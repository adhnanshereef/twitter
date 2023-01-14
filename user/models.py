from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, Permission

# User Model
class User(AbstractBaseUser):
    username = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    has_perm = models.ManyToManyField(Permission,  related_name='permissions', blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email',]
    objects = UserManager()
    def __str__(self):
        return self.username

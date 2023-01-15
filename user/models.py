from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

# User Model


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=20, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'email',]
    objects = UserManager()
    def __str__(self):
        return self.username


# def has_perm(self, perm, obj=None):
#     return self.is_superuser

# def has_module_perms(self, app_label):
#     return self.is_superuser
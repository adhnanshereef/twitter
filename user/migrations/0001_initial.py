# Generated by Django 4.1.5 on 2023-02-25 07:31

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("username", models.CharField(max_length=30, unique=True)),
                ("name", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("bio", models.TextField(blank=True, max_length=160)),
                (
                    "website",
                    models.URLField(
                        blank=True, validators=[django.core.validators.URLValidator()]
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=30)),
                (
                    "dateofbirth",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("joined", models.DateTimeField(auto_now_add=True)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "avatar",
                    models.ImageField(
                        default="avatar/avatar.svg", null=True, upload_to="avatar/"
                    ),
                ),
                ("theme", models.CharField(blank=True, default="light", max_length=10)),
                ("is_staff", models.BooleanField(blank=True, null=True)),
                ("is_superuser", models.BooleanField(blank=True, null=True)),
                (
                    "followers",
                    models.ManyToManyField(
                        blank=True, related_name="folower", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "following",
                    models.ManyToManyField(
                        blank=True, related_name="folowing", to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

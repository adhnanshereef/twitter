# Generated by Django 4.1.5 on 2023-02-20 16:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_user_followers_user_following"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="followers",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]

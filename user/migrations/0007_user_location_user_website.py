# Generated by Django 4.1.5 on 2023-02-25 05:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_user_followers_alter_user_following"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="location",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="website",
            field=models.URLField(
                blank=True,
                null=True,
                validators=[django.core.validators.URLValidator()],
            ),
        ),
    ]

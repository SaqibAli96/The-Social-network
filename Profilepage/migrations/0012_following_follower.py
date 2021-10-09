# Generated by Django 3.1.1 on 2020-12-04 22:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profilepage', '0011_auto_20201205_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='follower',
            field=models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL),
        ),
    ]

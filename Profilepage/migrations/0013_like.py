# Generated by Django 3.1.1 on 2020-12-20 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profilepage', '0012_following_follower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Profilepage.post')),
                ('user', models.ManyToManyField(related_name='linkingUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

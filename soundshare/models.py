from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    USER_TYPE = (
        ('Creator', 'Creator'),
        ('Listener', 'Listener'),
        ('Producer', 'Producer'),
    )

    username_text = models.CharField(max_length=64)
    email_text = models.CharField(max_length=64)
    password_text = models.CharField(max_length=64)
    firstname_text = models.CharField(max_length=64)
    lastname_text = models.CharField(max_length=64)
    type = models.CharField(max_length=6, choices=USER_TYPE, default='Listener')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=200,
                              verbose_name='Profile photo')

    def __str__(self):
        return self.username_text


class Song(models.Model):
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    creator = models.ManyToManyField(UserProfile)
    average_rating = models.IntegerField(default=0)
    album_title = models.CharField(max_length=64)
    link = models.URLField(unique=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title



from __future__ import unicode_literals
from django.db import models

# Song model
class Song(models.Model):
    song_name = models.CharField(max_length=100, null=True)
    duration = models.PositiveIntegerField(max_length=5, null=True)
    upload_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.song_name

class Podcast(models.Model):
    podcast_name = models.CharField(max_length=100, null=True)
    duration = models.PositiveIntegerField(max_length=5, null=True)
    upload_time = models.DateTimeField(auto_now_add=True, null=True) 
    host = models.CharField(max_length=100, null=True)
    participants = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.podcast_name

class AudioBook(models.Model):
    title = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=100, null= True)
    narrator = models.CharField(max_length=100, null=True)
    duration = models.PositiveIntegerField(max_length=5, null=True)
    upload_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title


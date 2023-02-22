from django.db import models
from django.contrib.auth.models import User

class Chart(models.Model):
    decade = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Charts'
        ordering = ['decade']
    
    def __str__(self):
        return f'{self.decade}'

class Song(models.Model):
    decade = models.ForeignKey(Chart, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False)
    artist = models.CharField(max_length=100, null=False)
    album = models.CharField(max_length=100, null=True, blank=True)
    rank = models.IntegerField(default=0)
    video_link = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'"{self.title}" by {self.artist}'

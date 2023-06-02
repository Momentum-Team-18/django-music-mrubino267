from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(to="Artist", on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    label = models.ForeignKey(
        to="Label", on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='media/images/')


    def __str__(self):
        return self.title


class Label(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
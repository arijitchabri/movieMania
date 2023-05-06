from django.db import models

# Create your models here.

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    image = models.ImageField()

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    duration = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    image = models.ImageField()

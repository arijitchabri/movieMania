from django.db import models

# Create your models here.

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Channel Name')
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return f'{self.id} {self.name}'

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Movie Name')
    duration = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name} {self.duration} {self.channel.name}'

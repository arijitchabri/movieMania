from django.db import models

# Create your models here.

class Channel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Channel Name')
    description = models.TextField()
    image = models.ImageField(upload_to='channel_images/', default='channel_images/channel.png', null=False)

    def __str__(self):
        return f'{self.id} {self.name}'
    
    def get_channel_id():
        return id

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='Movie Name')
    duration = models.IntegerField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie_images/', default='movie_images/movie.png', null=False)

    def __str__(self):
        return f'{self.name} {self.duration} {self.channel.name}'

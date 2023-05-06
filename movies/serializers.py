from rest_framework import serializers
from .models import *

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Channel
        fields = '__all__'

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    channel = ChannelSerializer()
    class Meta:
        model = Movie
        fields = '__all__'

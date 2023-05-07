from rest_framework import viewsets, permissions
from .models import Channel, Movie
from .serializers import ChannelSerializer, MovieSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('channel_id')
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def movieFilter(request, channel):
    channel_obj = get_object_or_404(Channel, name=channel)
    movies = Movie.objects.filter(channel=channel_obj)
    serializer = MovieSerializer(movies, many=True)
    return JsonResponse({'movies':serializer.data})

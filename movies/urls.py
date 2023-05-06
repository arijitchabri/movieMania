from django.urls import path, include
from rest_framework import routers
from .views import ChannelViewSet, MovieViewSet

router = routers.DefaultRouter()
router.register(r'channels', ChannelViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

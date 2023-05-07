from django.urls import path, include
from rest_framework import routers
from .views import ChannelViewSet, MovieViewSet, movieFilter

router = routers.DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'', ChannelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('channels/<str:channel>/', movieFilter, name='Movie filter'),

]

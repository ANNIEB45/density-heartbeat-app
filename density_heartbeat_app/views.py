from rest_framework import viewsets

from .models import Sensor, Heartbeat
from .serializers import SensorSerializer, HeartbeatSerializer, FeedSerializer

class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class HeartbeatView(viewsets.ModelViewSet):
    queryset = Heartbeat.objects.all()
    serializer_class = HeartbeatSerializer


class FeedView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = FeedSerializer
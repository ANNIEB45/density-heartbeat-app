from rest_framework import serializers
from .models import Sensor, Heartbeat

class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'

# class FeedSerializer(serializers.ModelSerializer):
#     heartbeats = HeartbeatSerializer(many=True, read_only=True)
#     sensor = SensorSerializer(many=True, read_only=True)

#     class Meta:
#         model
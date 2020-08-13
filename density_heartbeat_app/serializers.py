from rest_framework import serializers
from .models import Sensor, Heartbeat

# creating heartbeat and sensor serializer
# heartbeat serializer is first because it's a child of sensor
# all data from model will be exported to serializer for view

class HeartbeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heartbeat
        fields = '__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


# Will add feed data for front-end(homepage)

# class FeedSerializer(serializers.ModelSerializer):
#     heartbeats = HeartbeatSerializer(many=True, read_only=True)
#     sensor = SensorSerializer(many=True, read_only=True)

#     class Meta:
#         model
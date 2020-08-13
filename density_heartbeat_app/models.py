from django.db import models

# Creating models for heartbeat and sensor
# Heartbeat is a child of sensor

# Sensor model fields
    # alive-boolean
    # checking in-boolean, timestamp
class Sensor(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250) 
    isalive = models.CharField(max_length=250)
    check_in = models.CharField(max_length=250)


# Heartbeat model fields
    # beats- foreignkey
class Heartbeat(models.Model):
    rhythm = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='heartbeat')


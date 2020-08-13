from django.db import models

# Creating models for heartbeat and sensor
# Heartbeat is a child of sensor

# Sensor model fields
    # alive-boolean
    # checking in-boolean, timestamp
class Sensor(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250) 
    is_alive = models.CharField(max_length=250)
    check_in = models.CharField(max_length=250)

    def __str__(self):
        return self.name


# Heartbeat model fields
    # beats- foreignkey
class Heartbeat(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='heartbeat')


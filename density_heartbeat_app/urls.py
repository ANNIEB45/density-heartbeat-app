from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

# first parameter is url, second is data importing
router.register('sensor', views.SensorView)
router.register('heartbeat', views.HeartbeatView)

urlpatterns = [
    path('', include(router.urls))
]
"""density_heartbeat_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin

# bug-File "/Users/annebellefleur/density_assignment/density_heartbeat_project/urls.py", line 19, in <module>
#     from . import views
# ImportError: cannot import name 'views' from 'density_heartbeat_project' (/Users/annebellefleur/density_assignment/density_heartbeat_project/__init__.py)

    # can't figure out proplem
    # FIXED IT...THANK GOD... ADDED VIEWS FILE TO PROJECT FOLDER... 
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FrontendAppView.as_view()),
    path('api/v1/', include('density_heartbeat_app.urls')),
    re_path(r'^.*$', views.FrontendAppView.as_view()),
    
]


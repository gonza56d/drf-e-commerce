from django.urls import include
from rest_framework.routers import re_path


urlpatterns = [
    re_path(r'^', include('djoser.urls.authtoken')),
]

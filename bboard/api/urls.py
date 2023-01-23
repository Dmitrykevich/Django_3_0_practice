from django.urls import path

from .views import bbs


app_name = 'api'


urlpatterns = [
    path('bbs/', bbs),
]

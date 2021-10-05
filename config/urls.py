from app.views import hello_streams, streams
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('<name>/', hello_streams, name="stream"), 
    path('', streams)
]

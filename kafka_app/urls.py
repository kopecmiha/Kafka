from django.urls import path
from .views import kfk, cons

urlpatterns = [
    path('kfk/', kfk),
    path('cons/', cons),
]
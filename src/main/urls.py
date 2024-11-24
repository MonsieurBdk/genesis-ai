
from django.urls import path, include
from main.views import *

from ui import settings

from main.views import predict, main

urlpatterns = [
    path('', main, name="index"),
    path('predict/', predict, name='predict'),
] 

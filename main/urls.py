
from django.urls import path, include
from main.views import *

from ui import settings

urlpatterns = [
    path('', main, name="index"),
] 

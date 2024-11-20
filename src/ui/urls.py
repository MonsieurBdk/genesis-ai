from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from ui import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
] 

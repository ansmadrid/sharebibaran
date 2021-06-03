
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('share_detail.urls')),
    path('admin/', admin.site.urls),
]

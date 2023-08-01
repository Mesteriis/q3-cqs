from django.urls import path, include

from .v1 import urlpatterns as v1_urls

app_name = 'api'
urlpatterns = [
    path('api/v1/', include(v1_urls)),
]

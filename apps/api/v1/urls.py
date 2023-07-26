from rest_framework.routers import SimpleRouter
from .files import CodeFileViewSet
from django.urls import path, include

router = SimpleRouter()


router.register('files', CodeFileViewSet, basename='files')


urlpatterns = [
    path('v1/', include(router.urls)),
]
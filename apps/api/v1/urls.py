from rest_framework.routers import SimpleRouter
from .files import CodeFileViewSet
from .reports import ReportViewSet
from django.urls import path, include

router = SimpleRouter()


router.register('files', CodeFileViewSet, basename='files')
router.register('reports', ReportViewSet, basename='reports')


urlpatterns = [
    path('', include(router.urls)),
]

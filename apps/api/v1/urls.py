from rest_framework.routers import SimpleRouter
from .files import CodeFileViewSet
from django.urls import path, include

from .files import views

router = SimpleRouter()
router.register('files', CodeFileViewSet, basename='files')

urlpatterns = [
    path('files/<uuid:pk>/', views.CodeFileDetailView.as_view()),
    path('', include(router.urls)),
]

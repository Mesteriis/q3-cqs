from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import CodeFileSerializer, CodeFile

class CodeFileViewSet(
    CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet
):
    queryset = CodeFile.objects.all()
    serializer_class = CodeFileSerializer

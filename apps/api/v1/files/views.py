from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from .forms import UploadFileForm
from .serializers import CodeFileSerializer, CodeFile


class CodeFileViewSet(
    CreateModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet
):
    serializer_class = CodeFileSerializer

    def get_queryset(self):
        return CodeFile.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = CodeFile(file=request.FILES['file'], user=request.user)
            instance.save()
            return HttpResponseRedirect(request.path_info)
        return HttpResponseRedirect(request.path_info)

    def list(self, request, *args, **kwargs):
        form = UploadFileForm()
        files_list = self.get_queryset()
        for file in files_list:
            file.file = str(file.file).split('/')[-1]

        return render(request, 'upload.html', {'files_list': files_list, 'form': form})

from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import ReportSerializer, Report
from .forms import CreateReportForm
from files.models import CodeFile


class ReportViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet
):
    serializer_class = ReportSerializer

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        form = CreateReportForm(user=request.user)
        return render(request, 'reports.html', {'reports_list': self.get_queryset(), 'form': form})

    def create(self, request, *args, **kwargs):
        instance = Report(
                file=CodeFile.objects.get(file=request.POST['files']),
                user=request.user
        )
        instance.save()

        return HttpResponseRedirect(request.path_info)

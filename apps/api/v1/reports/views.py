from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from files.models import CodeFile
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
import subprocess

from .forms import CreateReportForm
from .serializers import ReportSerializer, Report
from reports.models import Status


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
        try:
            instance = Report(
                file=CodeFile.objects.get(file=request.POST['files']),
                user=request.user
            )
            instance.save()
        except:
            return HttpResponseRedirect(request.path_info)
        return HttpResponseRedirect(request.path_info)

    def retrieve(self, request, *args, **kwargs):
        return render(request, 'report.html', {'report': self.get_object()})

    @action(detail=True, methods=['POST'], name='review')
    def review_report(self, request, pk=None):
        report = Report.objects.get(pk=pk)
        var = subprocess.Popen(['flake8', f'./{report.file.file}'], stdout=subprocess.PIPE)
        errors_list = (var.communicate()[0].decode('utf-8').split('\n'))
        result = []
        for error in errors_list[:-1]:
            error = error.split(':')
            result.append(
                {
                    'line': error[1],
                    'column': error[2],
                    'error': ''.join(error[3:]),
                    'check_time': datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
                }
            )

        report.result = result
        report.status = Status.reviewed
        report.save()

        return HttpResponseRedirect(reverse_lazy('api:reports-list'))

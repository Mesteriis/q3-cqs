from rest_framework import serializers

from apps.api.v1.reports.serializers import ReportSerializer
from apps.files.models import CodeFile
from apps.reports.models import Report


class CodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFile
        fields = '__all__'


class CodeFileRetrieveSerializer(serializers.ModelSerializer):
    checks = serializers.SerializerMethodField()
    last_check = serializers.SerializerMethodField()

    class Meta:
        model = CodeFile
        fields = ('uid', 'file', 'last_check', 'checks')

    def get_checks(self, obj):
        checks = Report.objects.filter(file=obj)
        return ReportSerializer(checks, many=True).data

    def get_last_check(self, obj):
        if (
            latest_report := Report.objects.filter(file=obj)
            .order_by('-created')
            .first()
        ):
            return latest_report.created
        return None

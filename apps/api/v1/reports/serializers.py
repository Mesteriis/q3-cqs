from rest_framework import serializers
from reports.models import Report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['file', 'user', 'result', 'status', 'created', 'is_sent']

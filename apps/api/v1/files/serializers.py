


from rest_framework import serializers
from files.models import CodeFile


class CodeFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeFile
        fields = '__all__'
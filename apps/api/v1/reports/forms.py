from django import forms
from files.models import CodeFile


class CreateReportForm(forms.Form):
    files = forms.ModelChoiceField(queryset=CodeFile.objects.none())

    def __init__(self, user):
        super(CreateReportForm, self).__init__()
        self.fields['files'].queryset = CodeFile.objects.filter(user=user).values_list('file', flat=True)

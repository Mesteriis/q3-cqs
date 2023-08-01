from django import forms

from apps.users.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['email', 'password']


class UserAuthenticationForm(forms.Form):
    email = forms.EmailField(label='E-mail Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

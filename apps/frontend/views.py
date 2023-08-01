from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserAuthenticationForm
from apps.files.models import CodeFile
from apps.users.models import User
from apps.reports.models import Report


def registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('profile_view')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile_view')
            else:
                messages.error(request, 'Invalid email or password. Please try again.')
        else:
            messages.error(request, 'Something went wrong with login...')
    elif not request.user.is_authenticated:
        form = UserAuthenticationForm()
    else:
        return redirect('profile_view')
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login_view')


@login_required
def profile_view(request):
    user = request.user
    files = CodeFile.objects.filter(user=user)
    data = []
    for file in files:
        report = Report.objects.filter(file=file).order_by('-created').first()
        status = report.status if report else 'no reports yet'
        data.append({'file': file, 'status': status})
    return render(request, 'profile.html', {'user': user, 'files': data})

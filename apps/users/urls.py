from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from rest_framework import routers

from apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('register/', FormView.as_view(
        template_name='users/register.html',
        form_class=UserCreationForm,
        success_url='/',
    ), name='register'),
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html',
    ), name='login'),
    path('', include(router.urls)),
]

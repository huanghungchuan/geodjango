# accounts/urls.py
from django.urls import path

from .views import SignUpView, LoginForm, PasswordChangeForm
from django.contrib.auth.views import LoginView, PasswordChangeView



urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(form_class=LoginForm, template_name='registration/login.html'), name='login'),
    path('password_change/', PasswordChangeView.as_view(form_class=PasswordChangeForm, template_name='registration/password_change_form.html'), name='password_chage_form'),
]
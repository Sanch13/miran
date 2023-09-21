from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .views import registration, login

app_name = 'users'

urlpatterns = [
    path("registration/", registration, name='registration'),
    path("login/", login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password/",
         PasswordResetView.as_view(
             template_name='users/registration/password_reset_form.html',
             email_template_name='users/registration/password_reset_email.html'),
         name='password_reset'),
    path("reset_password_sent/",
         PasswordResetDoneView.as_view(
             template_name='users/registration/password_reset_done.html'),
         name='password_reset_done'),
    path("reset/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(
             template_name='users/registration/password_reset_confirm.html'),
         name="password_reset_confirm"),
    path("reset_password_complete",
         PasswordResetCompleteView.as_view(
             template_name='users/registration/password_reset_complete.html'),
         name="password_reset_complete"),
]

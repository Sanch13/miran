from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

app_name = 'users'

urlpatterns = [
    path("registration/", registration, name='registration'),
    path("login/", login, name='login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("reset_password/", PassResetView.as_view(), name='password_reset'),
    path("reset_password_sent/", PassResetDoneView.as_view(), name='password_reset_done'),
    path("reset/<uidb64>/<token>/", PassResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset_password_complete", PassResetCompleteView.as_view(), name="password_reset_complete"),

]

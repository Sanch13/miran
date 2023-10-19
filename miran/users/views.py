from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .forms import UserRegistrationForm, UserLoginForm


def home(request):
    context = {}
    return render(request=request,
                  template_name="users/base.html",
                  context=context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегистрировались! '
                             'Войдите под своим логином и паролем в систему')
            return redirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request=request,
                  template_name='users/registration/registration.html',
                  context=context)


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return redirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/registration/login.html', context=context)


class PassResetView(PasswordResetView):
    template_name = 'users/registration/password_reset_form.html'
    email_template_name = 'users/registration/password_reset_email.html'
    success_url = reverse_lazy("users:password_reset_done")


class PassResetDoneView(PasswordResetDoneView):
    template_name = 'users/registration/password_reset_done.html'


class PassResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/registration/password_reset_confirm.html'
    success_url = reverse_lazy("users:password_reset_complete")


class PassResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/registration/password_reset_complete.html'

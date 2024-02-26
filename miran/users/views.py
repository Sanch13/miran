from django.contrib import auth, messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

from .forms import UserRegistrationForm, UserLoginForm, UserChangePassForm, EditUserForm
from .models import User


def home(request):
    return redirect(to="books:book_list_card")


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request=request,
                             message='Вы успешно зарегистрировались! '
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
        request.session['email_user'] = request.POST["username"]
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                # Если user не авторизован и пытается взять книгу запоминаем его url. После
                # авторизации перенаправляем его на предыдущую страницу книги. Если user пришел не
                # с страницы книги перенаправляем его на список книг
                next_url = request.session.get('next_url', 'books:book_list_card')
                return redirect(next_url)
        else:
            messages.error(request=request,
                           message='Пожалуйста, введите правильный Email и пароль.')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request=request,
                  template_name='users/registration/login.html',
                  context=context)


def user_profile(request):
    user = get_object_or_404(User, email=request.user.email)
    form = EditUserForm(instance=user)

    if request.method == "POST":
        form = EditUserForm(data=request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data.get("first_name")
            user.last_name = form.cleaned_data.get("last_name")
            user.save()

    context = {
        "form": form
    }
    return render(request=request,
                  template_name="users/my_profile.html",
                  context=context)


class PassResetView(PasswordResetView):
    template_name = 'users/registration/password_reset_form.html'
    email_template_name = 'users/registration/password_reset_email.html'
    success_url = reverse_lazy("users:password_reset_done")

    def get(self, request, *args, **kwargs):
        context = {
            "email": request.session.get('email_user', '')
        }
        return render(request=request,
                      template_name='users/registration/password_reset_form.html',
                      context=context)


class PassResetDoneView(PasswordResetDoneView):
    template_name = 'users/registration/password_reset_done.html'


class PassResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/registration/password_reset_confirm.html'
    form_class = UserChangePassForm
    success_url = reverse_lazy("users:password_reset_complete")


class PassResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/registration/password_reset_complete.html'

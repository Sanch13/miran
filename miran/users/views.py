from django.contrib import auth, messages
from django.shortcuts import render, redirect
from django.urls import reverse

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
            print(form.errors)
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

""""
Представления для работы с регистрацией нового пользователя и входом на сайт
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm, UserRegisterForm

class CustomLoginView(LoginView):
    """"Кастомный класс для аутентификации пользователя"""
    form_class = CustomLoginForm
    template_name = 'login.html'
    authentication_form = AuthenticationForm


def user_register(request):
    """Функция регистрации пользователя"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
        else:
            return render(request, 'register.html', {'form': form})
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

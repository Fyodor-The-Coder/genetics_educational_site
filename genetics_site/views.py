""""Файл содержит логику вывода страницы для входа"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    """Функция выводит главную страницу сайта, если пользователь
    не зарегистрирован в текущей сессии"""
    return render(request, 'index.html')

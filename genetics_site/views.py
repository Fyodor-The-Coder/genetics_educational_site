from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def index(request):
    """Функция выводит главную страницу сайта"""
    return render(request, 'index.html')

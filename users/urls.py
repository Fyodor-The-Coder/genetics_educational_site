"""
URL-маршруты приложения 'users'.

Доступные пути:
- /login/ - страница входа
- /register/ - страница регистрации
"""

from django.urls import path
from .views import CustomLoginView, user_register

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', user_register, name='register'),
]

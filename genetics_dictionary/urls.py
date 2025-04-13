"""
URL-маршруты приложения 'genetics_dictionary'.

Доступные пути:
- /add/ - добавление термина
- /list/ - список терминов - словарь
"""

from django.urls import path
from .views import add_term, term_list

urlpatterns = [
    path('add/', add_term, name='add_term'),
    path('list/', term_list, name="terms_list")
]

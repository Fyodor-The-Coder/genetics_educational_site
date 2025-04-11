"""
Регистрация модели Term из models.py в административной панели Django
"""
from django.contrib import admin
from .models import Term

admin.site.register(Term)

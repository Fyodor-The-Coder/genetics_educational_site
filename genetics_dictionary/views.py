from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Term
from .forms import TermForm


def add_term(request):
    """Функция для добавления термина в словарь"""
    if request.method == "POST":
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Термин добавлен')
            return redirect('add_term')
        else:
            required_errors = any(
                error.code == 'required'
                for field in ['term_ru', 'term_definition']
                for error in form.errors.get(field, [])
            )

            if required_errors:
                messages.error(request, 'Не все обязательные поля заполнены')
            for error in form.errors.get('term_en', []):
                messages.error(request, f"Ошибка в английском названии: {error}")
    else:
        form = TermForm()
    return render(request, "add_term.html", {"form": form})

def term_list(request):
    """Функция выводит словарь терминов"""
    terms = Term.objects.all().order_by('term_ru')
    return render(request, "term_list.html", {"terms": terms})

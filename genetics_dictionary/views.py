from django.shortcuts import render, redirect
from .models import Term
from .forms import TermForm

def add_term(request):
    if request.method == "POST":
        form = TermForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect("terms_list")
    else:
        form = TermForm()
    return render(request, "add_term.html", {"form": form})

def term_list(request):
    terms = Term.objects.all().order_by('term_ru')
    return render(request, "term_list.html", {"terms": terms})
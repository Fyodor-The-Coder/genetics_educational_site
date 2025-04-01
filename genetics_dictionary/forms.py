from django import forms
from .models import Term

class TermForm(forms.ModelForm):
    class Meta:
        model = Term
        fields = ['term_id', 'term_ru', 'term_en', 'term_definition']
from django import forms
from django.core.exceptions import ValidationError
from .models import Term
import re
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column

class TermForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form-uniform'
        self.helper.layout = Layout(
            Row(
                Column(
                    Field('term_ru',
                          css_class='form-control-lg uniform-field'),
                    css_class='col-12 mb-4'
                ),
            ),
            Row(
                Column(
                    Field('term_en',
                          css_class='form-control-lg uniform-field'),
                    css_class='col-12 mb-4'
                ),
            ),
            Row(
                Column(
                    Field('term_definition',
                          css_class='form-control-lg uniform-field',
                          rows=4),
                    css_class='col-12 mb-4'
                ),
            ),
            Row(
                Column(
                    Submit('submit', 'Добавить термин',
                           css_class='btn-primary btn-lg uniform-btn'),
                    css_class='col-12 mb-3'
                ),
            )
        )

    class Meta:
        model = Term
        fields = ['term_ru', 'term_en', 'term_definition']
        labels = {
            'term_ru': 'Название термина на русском языке',
            'term_en': 'Название термина на английском языке',
            'term_definition': 'Определение термина'
        }

        def clean_term_en(self):
            term_en = self.cleaned_data.get('term_en')
            if term_en:
                # Проверка на наличие кириллических символов
                if re.search(r'[А-яЁ]', term_en):
                    raise ValidationError("Английское название содержит кириллические символы")

                # Проверка на наличие хотя бы одной латинской буквы
                if not re.search(r'[a-zA-Z]', term_en):
                    raise ValidationError("Должна быть хотя бы одна латинская буква")

            return term_en
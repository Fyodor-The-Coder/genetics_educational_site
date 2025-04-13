""""Формы для работы с пользовательским вводом"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    """"Форма для аутентификации пользователя"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Имя пользователя'
        self.fields['password'].label = 'Пароль'


class UserRegisterForm(UserCreationForm):
    """"Форма для корректной работы поля для добавления email
    на странице регистрации"""
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'example@mail.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

from django.shortcuts import render
# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


class PasswordChange(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:password_change_done.html')
    template_name = 'users/password_change.html'


class PasswordReset(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:password_reset_done.hmtl')
    template_name = 'users/password_form.html'


class PasswordResetConfirm(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:password_reset_complete.html')
    template_name = 'users/password_reset_confirm.html'

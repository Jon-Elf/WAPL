"""Этот модуль отвечает за формы"""
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class regForm(forms.Form):
    username = forms.CharField(label='username', max_length=16)
    password = forms.CharField(label='password', max_length=16, widget=forms.PasswordInput)
    second_password = forms.CharField(label='confirm password', max_length=16, widget=forms.PasswordInput)
    def clean(self):
        """функция для проверки пароля"""
        data = {
            'password': self.cleaned_data['password'],
            'second_password': self.cleaned_data['second_password'],
            'username': self.cleaned_data['username']
            }
        if data['password'] != data['second_password']:
            raise ValidationError('Ваши пароли не совпадают.')
        if len(data['password']) < 5:
            raise ValidationError('Ваш пароль должен содержать хотя бы 5 знаков.')
        return data


class journalForm(forms.Form):
    choice = forms.ChoiceField(choices=[
        ('week', 'week'),
        ('today', 'today')
    ])
    def clean_choice(self):
        data = self.cleaned_data['choice']
        return data

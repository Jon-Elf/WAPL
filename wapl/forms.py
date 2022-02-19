
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from .models import Plant, Action


class regForm(forms.Form):
    username = forms.CharField(label='username', max_length=16)
    password = forms.CharField(label='password', max_length=16, widget=forms.PasswordInput)
    second_password = forms.CharField(label='confirm password', max_length=16, widget=forms.PasswordInput)
    def clean(self):
        data = {
            'password': self.cleaned_data['password'],
            'second_password': self.cleaned_data['second_password'],
            'username': self.cleaned_data['username']
            }
        if data['password'] != data['second_password']:
            raise ValidationError('Passwords do not match')
        if len(data['password']) < 5:
            raise ValidationError('Your password must contain at least 5 characters')
        return data
	
class journalForm(forms.Form):
    choice = forms.ChoiceField(label='period', choices=[
        ('week', 'week'),
        ('today', 'today')
    ])
    def clean_choice(self):
        data = self.cleaned_data['choice']
        return data

class settimeForm(forms.Form):
    datetime = forms.TimeField(label='Watering time')
    time = forms.IntegerField(label='Watering duration (in sec)', max_value=300, min_value=1)
    activate =forms.BooleanField()
    def clean(self):
        data = {'datetime': self.cleaned_data['dateime'],
                'time': self.cleaned_data['time'],
                'activate': self.cleaned_data['activate']}
        return data

class createplantForm(forms.Form):
    name = forms.CharField(label='Name for the watering point', max_length=20)
    numb = forms.IntegerField(label='Channel number')
    datetime = forms.TimeField(label='Watering time', required=False)
    time = forms.IntegerField(label='Watering duration (in sec)',
                              max_value=300, min_value=1, required=False)


    def clean(self):
        data = {'name': self.cleaned_data['name'],
                'numb': self.cleaned_data['numb'],
                'datetime': self.cleaned_data['datetime'],
                'time': self.cleaned_data['time']}

        return data

class editplantForm(forms.Form):
    name = forms.CharField(label='Name for the watering point', max_length=20, required=True)
    numb = forms.IntegerField(label='Channel number', required=True)
    datetime = forms.TimeField(label='Watering time', required=False)
    time = forms.IntegerField(label='Watering durations (in sec)',
                              max_value=300, min_value=1, required=False)

    def cleaned_datetime(self):
        if 'datetime' not in self.cleaned_data:
            raise ValidationError('Wrong value for watering time')
        if self.cleaned_data['datetime']:
            data = {'datetime': self.cleaned_data['datetime']}
        else:
            data = {'datetime': self.cleaned_data[None]}
        return data

    def cleaned_time(self):
        if self.cleaned_data['time']:
            data = {'time': self.cleaned_data['time']}
        else:
            data = {'time': self.cleaned_data[None]}
        return data

    def cleaned_name(self):
        data = {'name': self.cleaned_data['name'].strip()}
        return data


class wateringForm(forms.Form):
    time = forms.IntegerField(label='Watering duration (in sec)',
                              max_value=300, min_value=1, required=False)
    def clean_time(self):
        data = {'time': self.cleaned_data['time']}

        return data

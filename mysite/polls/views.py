"""модуль отвечающий за вьюшки"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from operator import itemgetter
import os
from .forms import *
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Plant, Action
import datetime
from django.utils import timezone


@login_required
def index(request):
    print(request.user)
    return render(request, 'polls/index.html')

def reg(request):
    if not User.objects.all():
        if request.method == 'POST':
            form = regForm(request.POST)
            if form.is_valid():
                print(form.data)
                user = User.objects.create_superuser(form.data['username'], '', form.data['password'])
                user.save()
                print(User.objects.all())
                messages.success(request, 'Вы успешно зарегестрировались!')
                return redirect('/')
        else:
            form = regForm()
    else:
        return redirect('/')

    return render(request, 'polls/reg.html', {
        'form': form
    })

@login_required
def journal(request, name):
    plant = get_object_or_404(Plant, pk=name)

    if request.method == 'POST':
        a = Action(plant=plant, user=request.user, date=timezone.now(), time=5)
        a.save()
        print('\n\n\nПоливаю растение...\n\n\n')
        return redirect(request.path)


    form = journalForm()
    actions = Action.objects.filter(plant=plant, date__gt=timezone.now() - datetime.timedelta(days=1))
    if 'choice' in request.GET:
        form = journalForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['choice'] == 'week':
                actions = Action.objects.filter(plant=plant, date__gt=timezone.now() - datetime.timedelta(days=7))

    return render(request, 'polls/journal.html', {
        'actions': actions,
        'plant': plant,
        'form': form
        })

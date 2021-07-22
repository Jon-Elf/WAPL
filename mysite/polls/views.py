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
    dates = []
    for plant in Plant.objects.all():
        dates.append({'name': plant.name, 'last_watering': plant.last_watering()})
    return render(request, 'polls/index.html', {
        'plants': Plant.objects.all(),
        'dates': dates
    })

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

@login_required
def createplant(request):
    if request.method=='POST':
        form = createplantForm(request.POST)
        if form.is_valid():
            print('добавляю растение')
            p = Plant(name=form.cleaned_data['name'], numb=form.cleaned_data['numb'],
                      time=form.cleaned_data['time'], datetime=form.cleaned_data['datetime'])
            p.save()
            messages.success(request, 'Растение успешно добавлено')
            return redirect('/')
    else:
        form = createplantForm()
    return render(request, 'polls/createplant.html', {
            'form': form
            })


#def fff(request):
#
#    if request.method == 'post':
#        form = HBBNForm(request.POST)
#        if form.is_valid():
#
#
#            return redirect()
#    else:
#        form = JHGUHJNForm()
#    return render()

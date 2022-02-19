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
from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict


@login_required
def index(request):
    return render(request, 'wapl/index.html', {
        'plants': Plant.objects.filter(is_active=True),
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
                messages.success(request, 'You have successfully registered!')
                return redirect('/')
        else:
            form = regForm()
    else:
        return redirect('/')

    return render(request, 'wapl/reg.html', {
        'form': form
    })

@login_required
def journal(request, id):
    plant = get_object_or_404(Plant, pk=id, is_active=True)
    initial = model_to_dict(plant)
    if not initial['time']:
        initial['time'] = 30
    if request.method == 'POST':
        form_time = wateringForm(request.POST, initial=initial)
        if form_time.is_valid():
            if plant.actions.last():
                if plant.actions.last().done == 'in progress':
                    messages.success(request, 'Watering point already activated')
                    return redirect(request.path)

            a = Action(plant=plant, user=request.user, date=timezone.now(), time=form_time.data['time'])
            a.save()
            return redirect(request.path)

    form_time = wateringForm(initial=initial)
    button = True
    if plant.actions.last():
        if plant.actions.last().done == 'in progress':
            button = False

    form = journalForm()
    actions = Action.objects.filter(plant=plant, date__gt=timezone.now() - datetime.timedelta(days=1))
    if 'choice' in request.GET:
        form = journalForm(request.GET)
        if form.is_valid():
            if form.cleaned_data['choice'] == 'week':
                actions = Action.objects.filter(plant=plant, date__gt=timezone.now() - datetime.timedelta(days=7))

    return render(request, 'wapl/journal.html', {
        'actions': actions,
        'plant': plant,
        'form': form,
        'button': button,
        'form_time': form_time
        })

@login_required
def createplant(request):
    if request.method=='POST':
        form = createplantForm(request.POST)
        if form.is_valid():
            p = Plant(name=form.cleaned_data['name'], numb=form.cleaned_data['numb'],
                      time=form.cleaned_data['time'], datetime=form.cleaned_data['datetime'])
            if Plant.objects.filter(numb=form.cleaned_data['numb'], is_active=True).first():
                messages.warning(request, 'This channel is already in use in another watering point. This can lead to problems')
            p.save()
            messages.success(request, 'Watering point successfully created')
            return redirect('/')
    else:
        form = createplantForm()
    return render(request, 'wapl/createplant.html', {
            'form': form,
            })


@login_required
def removeplant(request, id):
    plant = get_object_or_404(Plant, pk=id, is_active=True)

    if request.method == 'POST':
        plant.is_active = False
        plant.save()
        return redirect('/')
    return render(request, 'wapl/removeplant.html', {
        'plant': plant
    })

@login_required
def editplant(request, id):
    plant = get_object_or_404(Plant, pk=id, is_active=True)
    initial = model_to_dict(plant)

    if request.method == 'POST':
        form = editplantForm(request.POST, initial=initial)
        if form.is_valid():

            plant.datetime = form.cleaned_data['datetime']
            plant.time = form.data['time']
            plant.name = form.data['name']
            plant.numb = form.data['numb']
            if not plant.datetime:
                plant.datetime = None
            if not plant.time:
                plant.time = None

            if Plant.objects.filter(numb=form.data['numb'], is_active=True).first():
                messages.warning(request, 'This channel is already in use in another watering point. This can lead to problems')
            plant.save()
            messages.success(request, 'Watering point successfully edited.')
            return redirect('/%s/journal' % id)

    else:
        form = editplantForm(initial=initial)
    return render(request, 'wapl/editplant.html', {
            'form': form,
            'plant': plant
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

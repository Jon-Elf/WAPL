"""модуль отвечающий за вьюшки"""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from operator import itemgetter
import os
from .forms import *
from datetime import datetime
from django.contrib import messages

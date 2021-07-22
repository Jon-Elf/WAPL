"""url для сайта"""
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('<int:name>/journal', views.journal, name='journal'),
    path('createplant', views.createplant, name='createplant')
]

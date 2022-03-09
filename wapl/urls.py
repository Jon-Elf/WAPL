from django.urls import path

from . import views

app_name = 'wapl'
urlpatterns = [
    path('', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('<int:id>/journal', views.journal, name='journal'),
    path('createplant', views.createplant, name='createplant'),
    path('<int:id>/removeplant', views.removeplant, name='removeplant'),
    path('<int:id>/editplant', views.editplant, name='editplant'),
    path('<int:number>/removechannel', views.removeChannel, name='removechannel'),
    path('addchannel', views.addChannel, name='addchannel'),
]

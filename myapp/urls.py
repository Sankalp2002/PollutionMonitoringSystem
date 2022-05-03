from django.contrib import admin
from django.urls import path
from myapp import views
from .check import tl

urlpatterns = [
    path('poldata/', views.polView),
    path('nodes/', views.showNodes, name='showNodes'),
    path('add/', views.addNode, name='addNode'),
    path('monitor/', views.monitorNodes, name='monitorNodes'),
    path('remove/<str:pid>', views.removeNode, name='removeNode'),
    path('edit/<str:did>', views.editNode, name='editNode'),
    path('display/<str:pid>', views.displayNode, name='displayNode'),
    path('edit/cancel', views.editNodecancel, name='editNodecancel'),
    #path('alertCheck', views.alertCheck, name='alertCheck'),
]

tl.start(block=False)

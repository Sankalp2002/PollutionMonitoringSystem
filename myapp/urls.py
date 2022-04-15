from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('poldata/', views.polView),
    path('nodes/', views.showNodes, name='showNodes'),
    path('add/', views.addNode, name='addNode'),
    path('remove/<str:pid>', views.removeNode, name='removeNode'),
    path('display/<str:pid>', views.displayNode, name='displayNode'),
]

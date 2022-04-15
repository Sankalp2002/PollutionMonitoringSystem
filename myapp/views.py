from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status
from .models import Pollution_Data,Node
from myapp.serializers import polSerializer
from rest_framework.decorators import api_view
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NewNodeForm

@api_view(['GET', 'POST', 'DELETE'])
def polView(request):
    if request.method == 'GET':
        p = JSONParser().parse(request)
        polobjects=Pollution_Data.objects.filter(node_Id=p['node_Id'])
        serializer=polSerializer(polobjects,many=True)
        print("getrequest")
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        p = JSONParser().parse(request)
        node=p['node_Id']
        serializer = polSerializer(data=p)
        if serializer.is_valid():
            if Node.objects.filter(node_Id=node).exists() and not Pollution_Data.objects.filter(datetime=p['datetime']).exists():
                serializer.save()
                obj=Node.objects.get(node_Id=node)
                if 'mq135' in p.keys():
                    obj.mq135=p['mq135']
                if 'mq5' in p.keys():
                    obj.mq5=p['mq5']
                if 'mq7' in p.keys():
                    obj.mq7=p['mq7']
                obj.save()
                print("postrequest")
                return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

def showNodes(request):
    if request.method == 'POST':
        return render(request, 'main.html',)
    else:
        nodes = Node.objects.all()
        return render(request, 'nodeList.html', {'nodes': nodes})

def displayNode(request,pid):
    if request.method == 'POST':
        return render(request, 'main.html',)
    else:
        node=Node.objects.get(node_Id=pid)
        return render(request, 'displayNode.html', {'node': node})

def addNode(request):
    form=NewNodeForm()
    if request.method=="POST":
        form= NewNodeForm(request.POST)
        if form.is_valid():
            n=form.save(commit=False)
            n.save()
            return HttpResponseRedirect(reverse('showNodes'))
        else:
            print('Error')
    return render(request,'newNode.html',{'form':form})

def removeNode(request,pid):
    Node.objects.get(node_Id=pid).delete()
    return HttpResponseRedirect(reverse('showNodes'))
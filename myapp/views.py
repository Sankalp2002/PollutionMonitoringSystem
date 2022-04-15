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
        polobjects=Pollution_Data.objects.all()
        serializer=polSerializer(polobjects,many=True)
        print("getrequest")
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        p = JSONParser().parse(request)
        serializer = polSerializer(data=p)
        if serializer.is_valid():
            serializer.save()
            print("postrequest")
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
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
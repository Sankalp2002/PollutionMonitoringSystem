from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from numpy import save
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
from .check import alertCheck
from datetime import datetime as dt,timedelta
from plotly.offline import plot
from plotly.graph_objs import Scatter
from django.db.models import Q

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
        serializer = polSerializer(data=p)
        mac=p['macAddress']
        obj=Node.objects.create(macAddress=mac)
        if serializer.is_valid():
            if not Pollution_Data.objects.filter(Q(macAddress=mac)&Q(datetimestamp=p['datetimestamp'])).exists():
                if Node.objects.filter(macAddress=mac).exists():
                    obj=Node.objects.get(macAddress=mac)
                    serializer.node_Id=obj.node_Id
                    serializer.save()
                    obj.mq135=p['mq135']
                    obj.macAddress=p['macAddress']
                    obj.save()
                    print("postrequest")
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    d=p['datetimestamp']
                    mq=p['mq135']
                    mc=p['macAddress']
                    dobj=Pollution_Data.objects.create(datetimestamp=d,mq135=mq,macAddress=mc,save=False)
                    dobj.save()
                    obj.mq135=dobj.mq135
                    obj.macAddress=dobj.macAddress
                    obj.save()
                    print("postrequest")
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
            else:
                JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(serializer.errors)
            obj=Node.objects.get(macAddress=mc).delete()
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        pass

def showNodes(request):
    if request.method == 'POST':
        return render(request, 'main.html',)
    else:
        alertnodes,nodes= alertCheck()
        return render(request, 'nodeList.html', {'alertnodes':alertnodes,'nodes': nodes})

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
            node=n.node_Id
            form= NewNodeForm()
            return render(request,'newNode.html',{'form':form,'node': node})
        else:
            print('Error')
    else:
        return render(request,'newNode.html',{'form':form})

def monitorNodes(request):
    nodes=Node.objects.all()
    plots_dict={}
    for node in nodes:
        d = timedelta(days = 60)
        node_data=Pollution_Data.objects.filter(Q(macAddress=node.macAddress)&Q(datetimestamp__range=[dt.now()-d,dt.now()])).order_by('datetimestamp')
        #node_data=Pollution_Data.objects.filter(node_Id=node.node_Id).order_by('datetimestamp')
        #print(len(node_data))
        y=[]
        x=[]
        for d in node_data:
            y.append(d.mq135)
            x.append(d.datetimestamp)
        plot_div = plot([Scatter(x=x, y=y,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')
        plots_dict[node.node_Id]=plot_div
    return render(request, 'monitor.html', {'plots': plots_dict})
        

def removeNode(request,pid):
    Node.objects.get(node_Id=pid).delete()
    return HttpResponseRedirect(reverse('showNodes'))

def editNode(request,did):
    if request.method=='POST':
        location = request.POST.get('location')
        node=Node.objects.get(node_Id=did)
        node.location=location
        node.save()
        return HttpResponseRedirect(reverse('showNodes'))
    else:
        if did=='cancel':
            return HttpResponseRedirect(reverse('showNodes'))
        else:
            node=Node.objects.get(node_Id=did)
            return render(request,'editNode.html',{'node':node})

def editNodecancel(request):
    return HttpResponseRedirect(reverse('showNodes'))



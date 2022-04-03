from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.response import Response
from rest_framework import status
from myapp.models import Pollution_Data
from myapp.serializers import polSerializer
from rest_framework.decorators import api_view

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

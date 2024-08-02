from django.shortcuts import render
from .models import Student 
from .serializers import StudentSerializer 
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status


@api_view(['GET', 'POST'])  
def list(request): 
    if request.method=='GET':
        movies = Student.objects.all() 
        serializer=StudentSerializer(movies,many=True)
        return Response(serializer.data) 
    
    elif request.method=='POST':
        serializer=StudentSerializer(data=request.data) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data) 
        else: return Response(serializer.errors)

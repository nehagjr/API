from django.shortcuts import render
from  django.http import JsonResponse ,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from .views import *
import io

# Create your views here.
def stu_list(request):
    stu = Student.objects.all()
    # print(stu)
    serializer=StudentSerializer(stu,many=True)
    return JsonResponse(serializer.data,safe=False)   
# safe = False   ka matlab list of dictnary ka data access ke liye likte he


def stu_details(request,pk):
    user=Student.objects.get(id=pk)
    serializer=StudentSerializer(user)
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def list(request):
    if request.method =="GET":
        user = Student.objects.all()
        serializer_data = StudentSerializer(user,many=True)
        # print(serializer_data.data)
        json_data = JSONRenderer().render(serializer_data.data)
        return HttpResponse(json_data,content_type = 'application/json')
    
    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data) 
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')  

    elif request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"Data updated !!!"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')     
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json")
     
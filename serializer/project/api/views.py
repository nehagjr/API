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

@csrf_exempt
def stu_details(request,pk):
    if request.method == "GET":
        id =Student.objects.get(id=pk)
        if id:    
            user=Student.objects.get(id=pk)
            serializer=StudentSerializer(user)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        else:
            res={"msg":"id not exist in database"}
            return HttpResponse(res)
    
    elif request.method=="PUT":
        id=Student.objects.get(id=pk)
        if id:
            jsonData=request.body
            stream=io.BytesIO(jsonData)
            python_data=JSONParser().parse(stream)
            user=Student.objects.get(id=pk)
            serializer=StudentSerializer(user,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                res={'msg':"successful"}
                jsonData=JSONRenderer().render(res)
                return HttpResponse(jsonData,content_type="application/json")
            jsonData=JsonResponse().render(serializer.errors)
            return HttpResponse(jsonData,content_type="application/json")
        else:
            res = {'msg': 'id not exist in Database'}
            return JsonResponse(res)
    
    elif request.method == 'DELETE':
        id = python_data.get(id=pk)
        if id:
            stu = Student.objects.get(id=pk)
            stu.delete()
            res = {'msg': 'Data Deleted!!'}
            return JsonResponse(res, safe=False)
        else:
            res = {'msg': 'id not present in Database'}
            return JsonResponse(res)    

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
     

    # elif request.method == 'PATCH':
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     python_data = JSONParser().parse(stream)
    #     id = python_data.get('id')
    #     stu = Student.objects.get(id=id)
    #     serializer = StudentSerializer(stu, data=python_data, partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg':'Data partially Updated !!'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')
    #     json_data = JSONRenderer().render(serializer.errors)
    #     return HttpResponse(json_data, content_type='application/json') 

    elif request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        if id:
            stu = Student.objects.get(id=id)
            stu.delete()
            res = {'msg': 'Data Deleted!!'}
            return JsonResponse(res, safe=False)
        else:
            res = {'msg': 'id not present in Database'}
            return JsonResponse(res)


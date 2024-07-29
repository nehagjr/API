from django.shortcuts import render
from  django.http import JsonResponse ,HttpResponse
# Create your views here.
def student(r):
    return HttpResponse("hii")

def studentlist(r):
    return HttpResponse("hiii")
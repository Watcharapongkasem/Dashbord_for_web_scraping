from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def hello(request,id):
    return HttpResponse('Hello World'+str(id))

def act(request):
    return HttpResponse('act')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request ) :
    return render (request,'home.html',{'name':'shaju'})

def add(request) :
    val1 =int(request.POST["number1"])
    val2 = int(request.POST["number2"])
    result = val1 +val2

    return render (request,'result.html',{'result':result })
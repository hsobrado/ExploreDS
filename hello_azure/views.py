from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pandas as pd

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

def getDescription(request):
    file = "hello_azure/Seconds per task (historical).csv"
    df = pd.read_csv(file, header=1)
    description = df.describe().to_json()
    description = json.loads(description)
    return JsonResponse(description)

def getInfo(request):
    file = "hello_azure/Seconds per task (historical).csv"
    df = pd.read_csv(file, header=1)
    description = df.info().to_json()
    description = json.loads(description)
    return JsonResponse(description)

def getShape(request):
    file = "hello_azure/Seconds per task (historical).csv"
    df = pd.read_csv(file, header=1)
    description = df.shape().to_json()
    description = json.loads(description)
    return JsonResponse(description)

def getHead(request):
    file = "hello_azure/Seconds per task (historical).csv"
    df = pd.read_csv(file, header=1)
    description = df.head().to_json()
    description = json.loads(description)
    return JsonResponse(description)

def getTail(request):
    file = "hello_azure/Seconds per task (historical).csv"
    df = pd.read_csv(file, header=1)
    description = df.tail().to_json()
    description = json.loads(description)
    return JsonResponse(description)
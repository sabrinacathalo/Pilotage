from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from pilotageApp.models import DataPilotage, LastAction

def index(request):
    return HttpResponse("HELLO !")

def test(request):
    return HttpResponse("Test !")

@csrf_exempt
def synchroData(request):

    if request.method == 'POST':
        dataJson = request.body.decode('utf-8')
        data = json.loads(dataJson)

        dataDB = DataPilotage(
            temperature =  data["temperature"],
            humidite =  data["humidite"],
            date_time = datetime.datetime.now(),
            altitude =  data["altitude"],
            lumiere =  data["lumiere"],
        )
        dataDB.save()
    return JsonResponse({"message": "data posted"})

@csrf_exempt
def action(request):

    if request.method == 'POST':
        dataJson = request.body.decode('utf-8')
        data = json.loads(dataJson)

        action = LastAction(
            value = data["value"],
            date_time = datetime.datetime.now()
        )
        action.save()
    return JsonResponse({"message": "action posted"})

@csrf_exempt
def resetData(request):

    if request.method == 'POST':

        datas = DataPilotage.objects.all()
        for data in datas:
            data.delete()

    return JsonResponse({"message": "removed"})

def getLastAction(request):

    action = LastAction.objects.last()

    return JsonResponse({"value": action.value})

def dashboard(request):

    context = {}

    lastData = DataPilotage.objects.all().order_by('-date_time').first()
    datas = DataPilotage.objects.all().order_by('date_time')
    context["datas"] = datas
    context["lastData"] = lastData
    context['temperatures'] = [data.temperature for data in datas]
    context['lumiere'] = [data.lumiere for data in datas]
    context['humidite'] = [data.humidite for data in datas]
    context['altitude'] = [data.altitude for data in datas]
    context['date_times'] = [int(data.date_time.timestamp()) for data in datas]
    

    return HttpResponse(render(request, "pilotageApp/dashboard.html", context))
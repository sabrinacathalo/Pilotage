from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import datetime

from pilotageApp.models import DataPilotage

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
            date_time = datetime.datetime.fromtimestamp(int(data["date_time"])),
            altitude =  data["altitude"],
            lumiere =  data["lumiere"],
        )
        dataDB.save()
    return JsonResponse({"message": "data posted"})

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
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
            distance_obstacle =  data["distance_obstacle"],
            distance_altitude =  data["distance_altitude"],
            lumiere =  data["lumiere"],
        )
        dataDB.save()
    return JsonResponse({"message": "data posted"})

def dashboard(request):

    context = {}
    context["datas"] = DataPilotage.objects.all()
    return HttpResponse(render(request, "pilotageApp/dashboard.html", context))
from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO !")

def test(request):
    return HttpResponse("Test !")
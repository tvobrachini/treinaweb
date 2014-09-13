from django.http import HttpResponse
import datetime


def olaMundo(request):
    return HttpResponse("Olá Mundo!")


def dataAtual(request):
    now = datetime.datetime.now()
    html = "<em>Agora é %s.</em>" % now
    return HttpResponse(html)

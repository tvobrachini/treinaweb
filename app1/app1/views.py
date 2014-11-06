from django.http import HttpResponse
from django.shortcuts import render
import datetime


def olaMundo(request):
    return HttpResponse("Olá Mundo!")


def dataAtual(request):
    now = datetime.datetime.now()
    return render(request, 'data/data_atual.html', {'data_atual': now})


def dataMais(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    data = datetime.datetime.now() + datetime.timedelta(days=offset)
    html = "<em>Em %s dia(s), será %s.</em>" % (offset, data)
    return HttpResponse(html)

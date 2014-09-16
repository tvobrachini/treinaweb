from django.http import HttpResponse
import datetime


def olaMundo(request):
    return HttpResponse("Olá Mundo!")


def dataAtual(request):
    now = datetime.datetime.now()
    html = "<em>Agora é %s.</em>" % now
    return HttpResponse(html)


def dataMais(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    data = datetime.datetime.now() + datetime.timedelta(days=offset)
    html = "<em>Em %s dia(s), será %s.</em>" % (offset, data)
    return HttpResponse(html)

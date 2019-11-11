# Timeline view

from django.http import HttpResponse


def timeline_index(request):
    return HttpResponse("<h1> This is the Timeline app")
